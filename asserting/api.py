import requests

def call_rest_api():
    response = requests.get("http://localhost:3000")
    return response.json()