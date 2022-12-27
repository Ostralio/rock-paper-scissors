import requests
import json
import numpy
import cv2
from PIL import Image

url = 'http://127.0.0.1:5000/face_data'

with open('face\website\imgdata.json') as file:
    data = numpy.array(json.load(file))
file.close()

cv2.imwrite('GSimg.png', data)
img = cv2.imread('GSimg.png')
print('hi')