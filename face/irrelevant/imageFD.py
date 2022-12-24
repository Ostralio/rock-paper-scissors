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
imgPath = 'images/' + fileName + '.jpg'
FaceCascPath = 'haarcascade_frontalface_default.xml'
EyeCascPath = 'haarcascade_eye.xml'

# Load the cascade
face_cascade = cv2.CascadeClassifier(FaceCascPath)
eye_cascade = cv2.CascadeClassifier(EyeCascPath)
# Read the input image
img = cv2.imread(imgPath)
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces: image file, scaleFactor (how close/far ppl are from the camera, make this number higher for shots that are far from the camera), minNeighbors (minimum number of times it identifies it as a face, limits false positives)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
sorted(faces, key=(lambda x: x[2]*x[3]))
sorted(eyes, key=(lambda x: x[2]*x[3]))
# (x, y, w, h) = faces[0]
# cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# for (x1, y1, w1, h1) in eyes:
#     if((x <= x1 <= (x + w)) and (y <= y1 <= (y+h))):
#         cv2.rectangle(img, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 4)
# Display the output
# cv2.imshow('img', img)
# cv2.waitKey()

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    for (x1, y1, w1, h1) in eyes:
        #Any eye inside face
        # if((x <= x1 <= (x + w)) and (y <= y1 <= (y+h))):
        #     cv2.rectangle(img, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 4)
        #Any eye above mouth
        if((x <= x1 <= (x + w)) and (y <= y1 <= (y+h/2))):
            cv2.rectangle(img, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 4)

cv2.imshow('img', img)
cv2.waitKey()