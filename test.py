from pathlib import Path
from openai import OpenAI
import os
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


text = "'El trabajo los unirá,' ...pensó Dios... 'No pueden hacer sus herramientas, preparar y transportar la madera, construir sus casas, sembrar y recolectar sus cosechas, hilar y tejer, y hacer su ropa, cada uno solo por sí mismo.'"

speech_file_path = Path(__file__).parent / f"speech_test.mp3"
with client.audio.speech.with_streaming_response.create(
    model="tts-1-hd",
    voice='onyx',
    input=text
) as response:
    response.stream_to_file(speech_file_path)
