import streamlit as st
import requests

st.title("Chat IA --- Usando LLMs do Groq")

pergunta = st.text_input(
    "Digite sua pergunta:"
)

if st.button("Perguntar"):
   with st.spinner("Pesquisando e gerando resposta..."):
    if pergunta.strip() == "":
        st.warning("Digite uma pergunta válida.")
    else:
        try:
            resposta = requests.post(
                "http://localhost:8000/perguntar",
                json={
                    "pergunta": pergunta
                }
            )
            dados = resposta.json()
            st.write(dados["resposta"])
        except Exception as erro:
            st.error(f"Erro: {erro}")