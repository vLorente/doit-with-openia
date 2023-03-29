import openai
import os
from dotenv import load_dotenv
import typer
from rich import print
from rich.table import Table


def main():
    # Cargar variables de entorno
    load_dotenv('./.env.local')

    # Obtengo mi api del env
    API_KEY = os.getenv("API_KEY")

    openai.api_key = API_KEY

    print('[bold blue]Subete a la ola de la IA 🌊[/bold blue]')

    table = Table("Comando", "Descripción")
    table.add_row("adios", "Salir de la aplicación")
    table.add_row("nueva", "Crear una nueva conversación")
    print(table)
    print('\n[bold]*[/bold][italic]Recuerda que si no reinicias la conversiación, el asistente tendrá el contexto completo de lo que habléis.[/italic]')

    messages = []
    while True:
        
        # Interacción con el usuario
        prompt = _prompt()

        # Nueva conversación
        if prompt == 'nueva':
            print('🔵 Ok! Empezamos de nuevo')
            messages = []
            prompt = _prompt()

        # Generar pregunta para GPT
        messages.append({"role": "user", "content": prompt})
        completion = openai.ChatCompletion.create(model='gpt-3.5-turbo',
                                                messages=messages,
                                                max_tokens=1000)
        
        # Retroalimentación de la conversación mantenida hasta ahora
        response = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": response})

        
        print(response)


def _prompt() -> str:

    prompt = typer.prompt('\n¿Qué quieres saber?')

    if prompt == 'adios':
        # Pedir confirmación de usuario
        exit = typer.confirm(text="✋ ¿Estás seguro?",
                             default=True)
        if exit:
            print('[bold green]👋 Hasta pronto![/bold green]')    
            raise typer.Abort()
        # Si el usuario decide no filalizar, el proceso se repite 
        return _prompt()
    
    return prompt

if __name__ == '__main__':
    typer.run(main)