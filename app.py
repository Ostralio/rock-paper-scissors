from flask import Flask, request, url_for
from flask_cors import CORS
from PIL import Image
import numpy as np

# python -m flask run

app = Flask(__name__)
CORS(app)

@app.route('/face_data', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'ok and???'
    elif request.method == "POST":
        input = request.get_json(force=True)
        im = Image.fromarray(np.array(input))
        im.show()
        return 'hey'

@app.route("/")
def home():
    return "deez"

@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='face/website/images/monkey.ico')
    