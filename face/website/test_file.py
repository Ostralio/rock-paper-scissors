import requests
import json

url = 'http://127.0.0.1:5000/face_data'

with open('face\website\imgdata.json') as file:
    data = json.load(file)
file.close()

requests.post(url, json=data)