import openai
import requests
import json
import pprint

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    json={
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "What's does this man developing?!"}]
    },
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer MY_API_KEY"
    }
)

pprint.pprint(json.loads(response.content))