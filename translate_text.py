from pathlib import Path
from openai import OpenAI
import os
import sys
from dotenv import load_dotenv

def load_environment():
    load_dotenv()

def initialize_client():
    return OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def translate_text(client, text, target_language):
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": f"Translate the following story to simple {target_language}. Make sure it is easy for a beginner to understand, but keep it interesting and engaging!"},
        {"role": "user", "content": text}
    ],
    max_tokens=4000
    )

    translation = completion.choices[0].message.content
    return translation

def translate(filename, target_language):
    load_environment()
    client = initialize_client()

    
    with open(f"./text/{filename}_English.txt", 'r') as file:
        text = file.read()

    translated_text = translate_text(client, text, target_language)

    with open(f"./text/{filename}_{target_language}.txt", 'w+') as file:
        file.write(translated_text)