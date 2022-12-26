from flask import Flask, request
import requests


app = Flask(__name__)

@app.route('/face_data', methods=['GET', 'POST'])
def test():
   if request.method == 'GET':
       return 'ok and???'
   elif request.method == "POST":
       print(request.get_json(force=True))
       return 'hey'

@app.route("/")
def home():
    return "deez"