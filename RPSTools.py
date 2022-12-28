import numpy as np
import cv2
import os
import json

FaceCascPath = 'haarcascade_frontalface_default.xml'

# Takes Img Object and RPS choice, resizes then adds the face_obj to traindata with next number as name. 
# Adds RPS choice to labels dict.
# Returns the path of img added
def save2traindata(face_obj, choice):
    try:
        new_name = f'{str(max(map(lambda x: int(x.split(".png")[0]), os.listdir("FaceTrainData/images"))) + 1)}.png'   # Basically finds highest number +1 and adds .png
    except ValueError:
        new_name = '1.png'
    
    face_obj = cv2.resize(face_obj, (50, 50))
    cv2.imwrite(f'FaceTrainData/images/{new_name}', face_obj)

    data = None
    
    with open('FaceTrainData/labels.json', 'r') as file:
        data = json.load(file)
        data[new_name] = choice
        
    with open('FaceTrainData/labels.json', 'w') as file:
        json.dump(data, file)
    
    file.close()
    return f'FaceTrainData/images/{new_name}'


# Uses haarcascade to find largest face within image, crops img to just be face then regrayscales.
# Pushes data through save2traindata to return img path
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
        crop_img = cv2.cvtColor(img[y:y+h, x:x+w], cv2.COLOR_BGR2GRAY)
        return save2traindata(crop_img, choice)