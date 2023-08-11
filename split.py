from pydub import AudioSegment
import os

# Path to the input audio file (2-hour long)
input_audio_path = "/Users/avgr/Downloads/Nomme_2023_07_02.mp3"

# Output directory to save the chunks
output_directory = "/Users/avgr/nomme/"
os.makedirs(output_directory, exist_ok=True)

# Load the input audio
audio = AudioSegment.from_file(input_audio_path)

# Duration of each chunk in milliseconds (10 seconds)
chunk_duration = 10000  # 10 seconds

# Split the audio into chunks
num_chunks = len(audio) // chunk_duration
for i in range(num_chunks):
    start_time = i * chunk_duration
    end_time = start_time + chunk_duration
    chunk = audio[start_time:end_time]

    # Save the chunk to the output directory
    output_chunk_path = os.path.join(output_directory, f"chunk_{i + 1}.mp3")
    chunk.export(output_chunk_path, format="mp3")

print(f"{num_chunks} chunks created in {output_directory}")
