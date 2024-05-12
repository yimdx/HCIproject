import pyaudio
import wave


def catch_audio():
    # Constants
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    # THRESHOLD = 500
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

    wf = wave.open("output.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def play_audio(audio_data):
    CHUNK = 1024

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open the audio stream
    stream = p.open(format=p.get_format_from_width(audio_data.getsampwidth()),
                    channels=audio_data.getnchannels(),
                    rate=audio_data.getframerate(),
                    output=True)

    # Read data in chunks and play it
    data = audio_data.readframes(CHUNK)
    while data:
        stream.write(data)
        data = audio_data.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


if __name__ == "__main__":
    # catch_audio()
    audio_file_path = "output.wav"  
    audio_data = wave.open(audio_file_path, 'rb') 
    play_audio(audio_data)
