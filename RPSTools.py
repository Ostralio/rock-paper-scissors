import numpy as np
import cv2
import os
import json

def save2traindata(face_obj, choice):
    try:
        new_name = f'{str(max(map(lambda x: int(x.split(".png")[0]), os.listdir("FaceTrainData/images"))) + 1)}.png'   # Basically finds highest number +1 and adds .png
    except ValueError:
        new_name = '1.png'
    
    cv2.imwrite(f'FaceTrainData/images/{new_name}', face_obj)

    data = None
    
    with open('FaceTrainData/labels.json', 'r') as file:
        data = json.load(file)
        data[new_name] = choice
        
    with open('FaceTrainData/labels.json', 'w') as file:
        json.dump(data, file)
    
    file.close()
    return f'FaceTrainData/images/{new_name}'