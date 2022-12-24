import requests
import json

resp = requests.get('http://127.0.0.1:5500/test.html')
if resp.status_code == 200:
    print(resp.status_code)
    data = resp
    print(data.text)
else:
    print(resp.status_code)

