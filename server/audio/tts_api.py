import requests
import json

def alibaba_tts(text, access_key_id, access_key_secret):
    # API endpoint for Alibaba Cloud TTS
    url = "https://nls-gateway.cn-shanghai.aliyuncs.com/stream/v1/tts"

    # Prepare headers with the API credentials and content type
    headers = {
        'X-NLS-Token': '<your token here>',  # Token from Alibaba Cloud token service
        'Content-Type': 'application/json',
    }

    # Prepare the payload with parameters
    payload = {
        'appkey': '<your appkey here>',
        'text': text,
        'format': 'mp3',
        'voice': 'xiaoyun',  # You can choose different voices
        'sample_rate': 16000,
        'volume': 50,
        'speech_rate': 0,
        'pitch_rate': 0,
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        # Assuming the API returns an audio stream
        return response.content
    else:
        print("Failed to request TTS:", response.status_code)
        return None

# Example usage
tts_audio = alibaba_tts("Hello, this is a test message.", 'your_access_key_id', 'your_access_key_secret')
if tts_audio:
    with open('output_tts.mp3', 'wb') as audio_file:
        audio_file.write(tts_audio)
