import numpy as np
import cv2
import os
import sys

def save2traindata(face_obj):
    #new_name = max(os.listdir('FaceTrainData'), key=(lambda x: int(x.split('.png')[0])))
    try:
        new_name = f'{str(max(map(lambda x: int(x.split(".png")[0]), os.listdir("FaceTrainData"))) + 1)}.png'   # Basically finds highest number +1 and adds .png
    except ValueError:
        new_name = '1.png'
    
    cv2.imwrite(f'FaceTrainData/{new_name}', face_obj)