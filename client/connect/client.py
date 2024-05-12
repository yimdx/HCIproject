import asyncio
import websockets
import requests


# async def send_audio(websocket_url, audio_file_path):
#     async with websockets.connect(websocket_url) as websocket:
#         # Open the audio file
#         with open(audio_file_path, 'rb') as audio_file:
#             while (audio_data := audio_file.read(1024)):
#                 await websocket.send(audio_data)
#                 # Wait for server to confirm receipt
#                 response = await websocket.recv()
#                 print(f"Server response: {response}")

async def send_audio(server_url, wav_file_path):
    # Open the WAV file
    with open(wav_file_path, 'rb') as wav_file:
        # Prepare the file to be sent
        files = {'file': ("audio.wav", wav_file, "audio/wav")}

        # Send the POST request to the server
        response = requests.post(server_url, files=files)

        # Check the response status
        if response.status_code == 200:
            print("WAV file sent successfully")
        else:
            print(f"Failed to send WAV file: {response.status_code}")


def get_tts_results(api_url, text):
    response = requests.post(api_url, json={"text": text})
    if response.status_code == 200:
        # Assuming the server sends back a URL to the audio file or audio data
        return response.content
    else:
        print(f"Error: {response.status_code}")
        return None


# Example usage
websocket_url = 'http://10.176.34.117:8000/upload/'
audio_file_path = 'C:\\Users\\15957\\Desktop\\2023\\hci\\HCIproject\\data\\output.wav'
asyncio.run(send_audio(websocket_url, audio_file_path))

# api_url = 'http://10.176.34.117:8000/tts'
# text = "Hello, how can I help you today?"
# tts_audio = get_tts_results(api_url, text)
# if tts_audio:
#     # Save or play the audio
#     with open('output_tts.wav', 'wb') as f:
#         f.write(tts_audio)
