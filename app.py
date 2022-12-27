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
FaceCascPath = 'haarcascade_frontalface_default.xml'

def find_face(arr, choice):
    face_cascade = cv2.CascadeClassifier(FaceCascPath)
    img = cv2.imwrite('temp.png', arr)
    img = cv2.imread('temp.png')
    faces = face_cascade.detectMultiScale(img, 1.1, 4) # Might needa fiddle w the numbas
    os.remove('temp.png')
    
    if len(faces) == 0:
        return 0    # Error code?
    else:
        sorted(faces, key=(lambda x: x[2]*x[3]))
        x, y, h, w = faces[0]
        crop_img = img[y:y+h, x:x+w]
        return rpst.save2traindata(crop_img, choice)

@app.route('/face_data', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'ok and???'
    elif request.method == "POST":
        input = request.get_json(force=True)
        temp = find_face(np.array(input['img']), input['choice'])
        if temp != 0:
            face = np.asarray(Image.open(temp))
            # pump face thru neural net to get actual response
        return 'Yop'
    else:
        print('Error finding face')
        return 'Error'

@app.route("/")
def home():
    return "deez"
    