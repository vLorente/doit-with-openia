import openai
import os
from dotenv import load_dotenv

load_dotenv('./.env.local')

# Obtengo mi api del env
API_KEY = os.getenv("API_KEY")

print(API_KEY)

openai.api_key = API_KEY

while True:
    
    prompt = input('\n¿Qué quieres saber?: ')

    if prompt == 'adios':
        print('Hasta pronto!')    
        break
    
    completion = openai.ChatCompletion.create(model='gpt-3.5-turbo',
                                              messages=[{"role": "user", "content": prompt}])
    
    print(completion.choices[0].text)
