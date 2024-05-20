from pathlib import Path
from openai import OpenAI
import os
from dotenv import load_dotenv

def load_environment():
    load_dotenv()

def initialize_client():
    return OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def read_and_chunk_file(file_path, max_chunk_size=4096):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ''

    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) + 2 > max_chunk_size:
            chunks.append(current_chunk.strip())
            current_chunk = paragraph + '\n\n'
        else:
            current_chunk += paragraph + '\n\n'
    
    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks

def generate_speech(client, text, voice, file_path):
    with client.audio.speech.with_streaming_response.create(
        model="tts-1-hd",
        voice=voice,
        input=text,
    ) as response:
        response.stream_to_file(file_path)

def process_text_to_speech(file, title, author, target_language):
    load_environment()
    client = initialize_client()

    file_path = f"./text/{file}_{target_language}.txt"
    intro = """
    Welcome to Short Stories in Simple Spanish. Today's story is {title} by {author}. Translations and audio use the latest OpenAI models, and the accent should improve in the coming months.""".format(title=title, author=author)

    chunks = read_and_chunk_file(file_path)

    speech_file_path = Path(__file__).parent / f"audio/{file}/intro.mp3"
    generate_speech(client, intro, 'onyx', speech_file_path)

    for i, chunk in enumerate(chunks):
        speech_file_path = Path(__file__).parent / f"audio/{file}/contents/{i}.mp3"
        generate_speech(client, chunk, 'nova', speech_file_path)