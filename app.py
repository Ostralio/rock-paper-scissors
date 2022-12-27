from flask import Flask, request, url_for
from flask_cors import CORS
from PIL import Image
import cv2
import numpy as np

# python -m flask run

app = Flask(__name__)
CORS(app)
FaceCascPath = 'face\irrelevant\haarcascade_frontalface_default.xml'

def find_face(arr):
    face_cascade = cv2.CascadeClassifier(FaceCascPath)
    cv2.imwrite('GSimg.png', arr) #Scuffed but easiest way get to GS image from array in cv2 is to save and reopen ;/
    img = cv2.imread('GSimg.png')
    faces = face_cascade.detectMultiScale(img, 1.1, 4) # Might needa fiddle w the numbas
    
    if len(faces) == 0:
        return 0    # Error code?
    else:
        sorted(faces, key=(lambda x: x[2]*x[3]))
        x, y, h, w = faces[0]
        crop_img = img[y:y+h, x:x+w]
        cv2.imwrite('face.png', crop_img)
        return 1 #Success?


@app.route('/face_data', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'ok and???'
    elif request.method == "POST":
        input = request.get_json(force=True)
        if find_face(np.array(input)) == 1:
            face = np.ndarray.tolist(np.asarray(Image.open('face.png')))
            # pump face thru neural net to get actual response
            return 'Yop'
        else:
            print('Error finding face')
            return 'Error'

@app.route("/")
def home():
    return "deez"

@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='face/website/images/monkey.ico')
    