import json
import requests
import base64

def alibaba_asr(audio_path, access_key_id, access_key_secret):
    url = "https://nls-gateway.cn-shanghai.aliyuncs.com/stream/v1/asr"

    # Headers including the required authorization and content type
    headers = {
        'X-NLS-Token': '<your token here>',  # This token is obtained from the Alibaba Cloud Token service
        'Content-Type': 'application/json',
    }

    # Reading the audio file
    with open(audio_path, 'rb') as audio_file:
        audio_data = audio_file.read()

    # Encoding audio data to Base64
    audio_base64 = base64.b64encode(audio_data).decode('utf-8')

    # ASR request body
    payload = {
        'appkey': '<your appkey here>',
        'format': 'wav',  # Change this according to your audio file format
        'sample_rate': 16000,  # Ensure this matches your audio file's sample rate
        'enable_punctuation_prediction': True,
        'enable_inverse_text_normalization': True,
        'enable_voice_detection': False,
        'audio': audio_base64
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        if result['status'] == 20000000:
            return result['result']
        else:
            print("Error in speech recognition:", result['status_text'])
    else:
        print("Failed to connect to API:", response.status_code)

    return None

# Example usage
audio_path = 'path_to_your_audio_file.wav'
access_key_id = 'your_access_key_id'
access_key_secret = 'your_access_key_secret'
transcript = alibaba_asr(audio_path, access_key_id, access_key_secret)
print("Transcribed Text:", transcript)
