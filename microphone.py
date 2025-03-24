import pyaudio
import numpy as np

# Initialize microphone
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

print("Listening for sound...")

while True:
    data = np.frombuffer(stream.read(1024), dtype=np.int16)
    volume = np.linalg.norm(data)
    if volume > 20000:  # Adjust threshold
        print("Loud sound detected!")
