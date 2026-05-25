import streamlit as st
import requests
import time

st.set_page_config(
    page_title="Chat IA do Felipe",
    page_icon="🤖",
    layout="centered"
)

st.title("Chat IA com Groq")

# cria histórico
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# mostra mensagens antigas
for mensagem in st.session_state.mensagens:

    with st.chat_message(mensagem["role"]):

       st.write(mensagem["content"])

# input estilo chat
pergunta = st.chat_input(
    "Digite sua pergunta"
)

# quando usuário perguntar
if pergunta:

    # salva pergunta
    st.session_state.mensagens.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    # mostra pergunta
    with st.chat_message("user"):

        st.write(pergunta)

    # loading
    with st.spinner("Pensando..."):

       try:

        resposta = requests.post(
            "http://127.0.0.1:8000/perguntar",
            json={
                "pergunta": pergunta
            },
            timeout=60
        )

        resposta.raise_for_status()

        dados = resposta.json()

        resposta_ia = dados["resposta"]

       except Exception as erro:

        resposta_ia = f"Erro: {erro}"

    # salva resposta
    st.session_state.mensagens.append(
        {
            "role": "assistant",
            "content": resposta_ia
        }
    )

    # mostra resposta com efeito digitando
    with st.chat_message("assistant"):

        resposta_parcial = ""

        placeholder = st.empty()

        for palavra in resposta_ia.split():

            resposta_parcial += palavra + " "

            placeholder.markdown(
                resposta_parcial + "▌"
            )

            time.sleep(0.03)

        placeholder.markdown(resposta_parcial)