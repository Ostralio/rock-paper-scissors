from flask import Flask, request, render_template, send_from_directory
from flask_cors import CORS
from PIL import Image
import os
import cv2
import numpy as np
import RPSTools as rpst
import rpsModel as rps

# python -m flask run

app = Flask(__name__)
CORS(app)
model = rps.model()

@app.route('/face_data', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return 'ok and???'
    elif request.method == "POST":
        input = request.get_json(force=True)
        temp = rpst.save2traindata(rpst.find_face(np.array(input['img'])), input['choice'])
        print(temp)
        if temp != 0:
            MLarray = np.asarray(cv2.imread(temp, 0))
            predictionTuple = model.get_prediction(MLarray)
            print(predictionTuple)
            return predictionTuple[0]
        else:
            return 'error'
    
    else:
        return 'tf is that request brah'

@app.route("/cattle")
def train():
    if request.method == "GET":  
        model.train()
        return "yubba"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def home():
    return render_template("yuh.html")

if __name__ == "__main__":
	app.run()