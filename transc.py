from transformers import pipeline
import os

# Initialize the Whisper pipeline with your custom model
# whisper_pipeline = pipeline("automatic-speech-recognition", model="path_to_your_custom_model")
# whisper_pipeline = pipeline("automatic-speech-recognition", model="TalTechNLP/whisper-large-et")
# whisper_pipeline = pipeline("automatic-speech-recognition", model="arampacha/whisper-large-uk-2")
whisper_pipeline = pipeline("automatic-speech-recognition", model="Yehor/whisper-small-ukrainian")
# Path to the directory containing MP3 files
audio_dir = "output_chunks"

# Output file to save transcribed text
output_text_file = "raguli.txt"

def extract_number(filename):
    return int(filename.split("_")[1].split(".")[0])

mp3_files = [mp3_file for mp3_file in os.listdir(audio_dir) if mp3_file.endswith(".mp3")]
mp3_files = sorted(mp3_files, key=extract_number)

# Iterate over each MP3 file in the directory
with open(output_text_file, "w") as output_file:
    for mp3_file in mp3_files:
        if mp3_file.endswith(".mp3"):
            mp3_path = os.path.join(audio_dir, mp3_file)

            # Perform audio transcription using the Whisper pipeline
            transcription = whisper_pipeline(mp3_path)
            transcribed_text = transcription['text']

            print("\n" + mp3_file + "\n")

            print("\n" + transcribed_text  + "\n")

            # Write transcribed text to the output file with a line break separator
            output_file.write(transcribed_text + "\n" + "\n")

print("Transcription complete. Output saved to", output_text_file)
