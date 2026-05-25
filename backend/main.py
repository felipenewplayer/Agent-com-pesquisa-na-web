from groq import Groq
from ddgs import DDGS
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
Você é um assistente de IA amigável.

Responda de forma:
- natural
- curta quando possível
- objetiva
- sem criar tutoriais enormes sem necessidade

Se o usuário pedir código:
explique de forma clara e prática.

Pergunta:
{pergunta}

Informações:
{info}
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