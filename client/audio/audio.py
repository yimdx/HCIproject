import pyaudio

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1    
RATE = 44100  
CHUNK = 1024  
THRESHOLD = 500          
RECORD_SECONDS = 10      

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

frames = []

for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

with open('output.wav', 'wb') as f:
    for frame in frames:
        f.write(frame)

