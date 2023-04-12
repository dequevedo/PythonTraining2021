import os
import openai
import time

openai.api_key = "api_key"

player_prompt = "como fazer um for em python?"

start_time = time.time()
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é um personagem de um jogo. "
                                      "Você é um Rei de um reinado mediano. "
                                      "Dê respostas curtas de no máximo 3 sentenças."
                                      "Você jamais deve fugir do personagem."
                                      "Mantenha seu conhecimento de acordo com o conhecimento de uma pessoa do século 10."
                                      "Dependendo da resposta você pode ficar feliz ou bravo. "
                                      "Coloque essa palavra chave no final da resposta $X, "
                                      "onde X é o valor do humor e pode variar de -100 a 100"},
        {"role": "user", "content": "O jogador é seu filho e disse a você: " + player_prompt},
    ],
    temperature=0.4
)
end_time = time.time()

print(response.choices[0].message.content)
print(f"API response time: {end_time - start_time} seconds")
