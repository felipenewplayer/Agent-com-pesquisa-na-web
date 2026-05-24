from groq import Groq
from ddgs import DDGS
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


class Pergunta(BaseModel):
    pergunta: str


@app.get("/")
def home():
    return {"mensagem": "API funcionando"}

def busca_na_web(pergunta):
    resultados_texto = []

    with DDGS() as ddgs:

        resultados = ddgs.text(
            pergunta,
            max_results=5
        )

        for resultado in resultados:

            titulo = resultado.get("title", "")
            corpo = resultado.get("body", "")

            resultados_texto.append(
                f"Título: {titulo}\nConteúdo: {corpo}"
            )

    return "\n\n".join(resultados_texto)


def agente(pergunta):

    info = busca_na_web(pergunta)

    prompt = f"""
    Você é um agente inteligente especializado
    em responder perguntas.

    Pergunta do usuário:
    {pergunta}

    Informações encontradas na web:
    {info}

    Use as informações da web como apoio.

    Caso elas sejam insuficientes,
    utilize também seu conhecimento
    para responder da melhor forma possível.

    Responda de forma clara e objetiva.
    """

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content


@app.post("/perguntar")
def perguntar(dados: Pergunta):

    resposta = agente(dados.pergunta)

    return {
        "resposta": resposta
    }