import requests
import json

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=actual_api_key_here"  # Replace with your actual API key
headers = {'Content-Type': 'application/json'}
data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Explain how AI works in a few words"
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)