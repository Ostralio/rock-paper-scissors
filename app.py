from flask import Flask, request, url_for
from flask_cors import CORS
from PIL import Image
import cv2
import numpy as np
import RPSTools as rpst
import os

# python -m flask run

app = Flask(__name__)
CORS(app)

@app.route('/face_data', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'ok and???'
    elif request.method == "POST":
        input = request.get_json(force=True)
        temp = rpst.find_face(np.array(input['img']), input['choice'])
        if temp != 0:
            MLarray = np.asarray(cv2.imread(temp))
            # pump face thru neural net to get actual response
        return 'Yop'
    else:
        print('Error finding face')
        return 'Error'

@app.route("/")
def home():
    return "deez"