import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

resposta = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Você é um engenheiro DevOps especialista em Azure."},
        {"role": "user", "content": "Crie um aplicativo Python simples e publique no Azure."}
    ]
)

print(resposta.choices[0].message["content"])
