import requests
import json
import numpy
import cv2
from PIL import Image
import RPSTools as rpst

url = 'http://127.0.0.1:5000/face_data'

rpst.save2traindata(cv2.imread('FaceTrainData/1.png'))