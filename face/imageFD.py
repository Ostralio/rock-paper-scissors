import cv2
import numpy as np
import sys

# TAKE FACE IMAGE AND CONVERT TO DATA OF FACE STRUCTURE

# def imageFixer(path):
#     img = cv2.imread(path)
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('img', gray)
#     return gray

fileName = sys.argv[1]
imgPath = 'images/' + fileName + '.JPG'
cascPath = 'haarcascade_frontalface_default.xml'

# Load the cascade
face_cascade = cv2.CascadeClassifier(cascPath)
# Read the input image
img = cv2.imread(imgPath)
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces: image file, scaleFactor (how close/far ppl are from the camera, make this number higher for shots that are far from the camera), minNeighbors (minimum number of times it identifies it as a face, limits false positives)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()