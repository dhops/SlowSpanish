from pydub import AudioSegment
import os
import sys

def combine_mp3_files_from_folder(folder_path, output_file):
    combined = AudioSegment.empty()

    # Combine the intro.mp3 file
    intro_path = os.path.join(folder_path, 'intro.mp3')
    if os.path.exists(intro_path):
        intro_audio = AudioSegment.from_mp3(intro_path)
        combined += intro_audio
        silence = AudioSegment.silent(duration=2500)
        combined += silence
    else:
        print(f"Intro file not found: {intro_path}")
        return

    # Combine the content mp3 files
    content_folder_path = os.path.join(folder_path, 'contents/')
    if os.path.exists(content_folder_path):
        for file_name in sorted(os.listdir(content_folder_path)):
            if file_name.endswith(".mp3"):
                file_path = os.path.join(content_folder_path, file_name)
                audio = AudioSegment.from_mp3(file_path)
                combined += audio
    else:
        print(f"Content folder not found: {content_folder_path}")
        return

    combined.export(output_file, format="mp3")
    print(f"Combined file saved as {output_file}")