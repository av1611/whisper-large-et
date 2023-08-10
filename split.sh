#!/bin/bash

input_file="ole.mp3"    # Replace with your input MP3 file
output_format="chunk_%04d.mp3"
chunk_duration=20         # Duration of each chunk in seconds

# Create output directory if it doesn't exist
mkdir -p output_chunks

# Split the audio into chunks
ffmpeg -i "$input_file" -f segment -segment_time "$chunk_duration" -c copy "output_chunks/$output_format"

echo "Splitting complete."
