def tongyi_qianwen_llm(prompt, api_key):
    url = "https://api.tongyiqianwen.cn/llm/v1/requests"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    payload = {
        'prompt': prompt,
        'max_tokens': 150,
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['text'].strip()
    else:
        print("Failed to query LLM:", response.status_code)
        return None

# Example usage
llm_response = tongyi_qianwen_llm("Describe the implications of quantum computing on encryption.", '<your_api_key>')
print("LLM Response:", llm_response)
