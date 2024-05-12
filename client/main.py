from audio.audio import catch_audio, play_audio
from connect.client import send_audio, get_tts_results
import asyncio
import time


server_url = 'http://10.176.34.117:8000/upload/'


def main():
    while True:
        # Step 1: Capture audio
        command = input("Enter a command to start recording: s ")
        if command.lower() == "s":
            catch_audio()

            # Step 2: Send audio to server
            asyncio.run(send_audio(server_url, "output.wav"))

            # Step 3: Receive TTS result from server
            tts_result = get_tts_results()

            # Step 4: Play TTS result
            play_audio(tts_result)

            # Sleep for some time before repeating the loop
            time.sleep(5)  # Adjust as needed