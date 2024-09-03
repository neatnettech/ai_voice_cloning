import os
import librosa
import numpy as np
from pathlib import Path

# Define paths
RAW_AUDIO_DIR = Path("../data/raw")
PROCESSED_AUDIO_DIR = Path("../data/processed")

# Ensure processed directory exists
PROCESSED_AUDIO_DIR.mkdir(parents=True, exist_ok=True)

def normalize_audio(audio, target_db=-20):
    """Normalize the audio to a target decibel level."""
    gain = target_db - librosa.core.amplitude_to_db(np.max(np.abs(audio)))
    return audio * (10.0**(gain / 20.0))

def preprocess_audio(file_path):
    """Preprocess a single audio file."""
    audio, sr = librosa.load(file_path, sr=22050)
    audio = normalize_audio(audio)
    file_name = file_path.stem + "_processed.wav"
    librosa.output.write_wav(PROCESSED_AUDIO_DIR / file_name, audio, sr)

def preprocess_all_audio():
    """Preprocess all audio files in the raw directory."""
    for audio_file in RAW_AUDIO_DIR.glob("*.wav"):
        preprocess_audio(audio_file)

if __name__ == "__main__":
    preprocess_all_audio()
    print(f"Preprocessed audio files are saved in {PROCESSED_AUDIO_DIR}")