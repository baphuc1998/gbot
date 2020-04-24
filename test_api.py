import requests
import json
import time

url = "http://localhost:5005/webhooks/rest/webhook"
headers = {'Content-Type': "text/plain"}

message = 'Jarvis'
payload = '{"sender": "token", "message": "' + message + '"}'
# payload = '{"sender":{"sender_id":"Despaa Citooo","business":"","category":""},"message":"hi"}'
response = requests.request("POST", url, data=payload, headers=headers)
json_data = json.loads(response.text)
print(json_data)
print(json_data[0]['text'])