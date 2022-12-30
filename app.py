from flask import Flask, request, url_for
from flask_cors import CORS
from PIL import Image
import cv2
import numpy as np
import RPSTools as rpst
import os
import rpsModel as rps

# python -m flask run

app = Flask(__name__)
CORS(app)
model = rps.model()

@app.route('/face_data', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'ok and???'
    elif request.method == "POST":
        input = request.get_json(force=True)
        temp = rpst.save2traindata(rpst.find_face(np.array(input['img'])), input['choice'])
        
        if temp != 0:
            MLarray = np.asarray(cv2.imread(temp))
            return model.get_prediction(MLarray)
        else:
            return 'error'
    
    else:
        return 'tf is that request brah'

@app.route("/")
def home():
    return "deez"