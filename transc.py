from transformers import pipeline
import os


# Initialize the Whisper pipeline with your custom model
# whisper_pipeline = pipeline("automatic-speech-recognition", model="path_to_your_custom_model")
# whisper_pipeline = pipeline("automatic-speech-recognition", model="TalTechNLP/whisper-large-et")
# whisper_pipeline = pipeline("automatic-speech-recognition", model="arampacha/whisper-large-uk-2")
# whisper_pipeline = pipeline("automatic-speech-recognition", model="Yehor/whisper-small-ukrainian")
whisper_pipeline = pipeline("automatic-speech-recognition",
    model="Yehor/wav2vec2-xls-r-1b-uk-with-lm")

# whisper_pipeline = pipeline("automatic-speech-recognition", model="Yehor/wav2vec2-xls-r-300m-uk-with-news-lm")
# whisper_pipeline = pipeline("automatic-speech-recognition", model="Yehor/wav2vec2-xls-r-300m-uk-with-news-lm")
# whisper_pipeline = pipeline("automatic-speech-recognition", model="Yehor/wav2vec2-xls-r-300m-uk-with-news-lm")
# whisper_pipeline = pipeline("automatic-speech-recognition", model="Yehor/wav2vec2-xls-r-300m-uk-with-news-lm")

# Yehor/bn-base # retnd error on the 1st run, mbpi, m1

# Yehor/wav2vec2-xls-r-base-uk-with-cv-lm # 2h processed in 15 min
# Yehor/wav2vec2-xls-r-base-uk-with-small-lm # 2h processed in 15 min

# Yehor/wav2vec2-xls-r-300m-uk # # retnd error on the 1st run, m1
# Yehor/wav2vec2-xls-r-300m-uk-with-lm # 2h processed in 20 min
# Yehor/wav2vec2-xls-r-300m-uk-with-small-lm # 2h processed in 20 min
# Yehor/wav2vec2-xls-r-300m-uk-with-small-lm-noisy # 2h processed in 30 min

# Yehor/wav2vec2-xls-r-300m-uk-with-news-lm # 2h processed in 30 min
# Yehor/wav2vec2-xls-r-300m-uk-with-wiki-lm # 2h processed in 25 min
# Yehor/wav2vec2-xls-r-300m-uk-with-3gram-news-lm # 2h processed in 25 min
# Yehor/wav2vec2-xls-r-300m-uk-traced-jit # err, faild downld

# Yehor/wav2vec2-xls-r-1b-uk-with-lm # OK
# Yehor/wav2vec2-xls-r-1b-uk-with-news-lm
# Yehor/wav2vec2-xls-r-1b-uk-with-binary-news-lm

# Yehor/whisper-small-ukrainian

# Yehor/kenlm-ukrainian
# Yehor/indonesian-kenlm-newspapers

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
