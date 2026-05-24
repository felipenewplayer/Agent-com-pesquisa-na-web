import streamlit as st
import requests

st.title("Chat IA com Groq")

# cria histórico
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# mostra mensagens antigas
for mensagem in st.session_state.mensagens:

    with st.chat_message(mensagem["role"]):

        st.markdown(mensagem["content"])

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

    # mostra pergunta na tela
    with st.chat_message("user"):

        st.markdown(pergunta)

    # loading
    with st.spinner("Pensando..."):

        resposta = requests.post(
            "https://agent-com-pesquisa-na-web.onrender.com/perguntar",
            json={
                "pergunta": pergunta
            }
        )

        dados = resposta.json()

        resposta_ia = dados["resposta"]

    # salva resposta
    st.session_state.mensagens.append(
        {
            "role": "assistant",
            "content": resposta_ia
        }
    )

    # mostra resposta
    with st.chat_message("assistant"):

        st.markdown(resposta_ia)