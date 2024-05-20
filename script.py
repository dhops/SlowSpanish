from pathlib import Path
from openai import OpenAI
import os
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


filename = 'leyenda.txt'

def extract_names_and_texts(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Regex to find all occurrences of names in brackets and the following text
    pattern = re.compile(r'\[([^\]]+)\](.*?)(?=\[|$)', re.DOTALL)
    matches = pattern.findall(content)

    names = []
    texts = []

    for match in matches:
        names.append(match[0])
        texts.append(match[1].strip())

    return names, texts

names, texts = extract_names_and_texts(filename)
name_to_voice = {'Dios': 'onyx', 'Narrator': 'nova'} 
print(texts)
raise ValueError("Number of names and texts do not match")
if len(names) != len(texts):
    raise ValueError("Number of names and texts do not match")

for i in range(len(names)):
  speech_file_path = Path(__file__).parent / f"speech_{i}.mp3"
  with client.audio.speech.with_streaming_response.create(
    model="tts-1-hd",
    voice=name_to_voice[names[i]],
    input=texts[i],
  ) as response:
    response.stream_to_file(speech_file_path)
