from groq import Groq
from ddgs import DDGS
import os

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def busca_na_web(pergunta):
    resultados_texto = []

    with DDGS() as ddgs:
        resultados = ddgs.text(pergunta, max_results=5)

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
    Você é um agente inteligente.

    Pergunta:
    {pergunta}

    Informações encontradas:
    {info}

    Responda SOMENTE com base nessas informações.

    Se não houver resposta confiável, diga:
    "Não foi possível responder com precisão."
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


def perguntar():
    while True:
        pergunta = input("Você: ").strip()

        if pergunta != "":
            return pergunta

        print("Digite uma pergunta válida.")


resposta = agente(perguntar())

print("\nIA:")
print(resposta)