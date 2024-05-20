from record_audio import process_text_to_speech
from translate_text import translate
from combine_audio import combine_mp3_files_from_folder
import os

filename = "clockmaker"
title = "The Clockmaker"
author = "Robert Louis Stevenson"

os.mkdir(f"./audio/{filename}/")
os.mkdir(f"./audio/{filename}/contents/")

print("translating")
translate(filename, "Spanish")

print("recording")
process_text_to_speech(filename, title, author, "Spanish")

print("combining")
combine_mp3_files_from_folder("./audio/"+filename+"/", filename+".mp3")