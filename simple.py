from pathlib import Path
from openai import OpenAI
import os
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

with open('leyenda.txt', 'r') as file:
    text = file.read()

speech_file_path = Path(__file__).parent / f"simple.mp3"
with client.audio.speech.with_streaming_response.create(
    model="tts-1-hd",
    voice='nova',
    speed=0.7,
    input=text[:1000]
) as response:
    response.stream_to_file(speech_file_path)
