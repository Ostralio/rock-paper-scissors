import json
from PIL import Image
import numpy

with open('face\website\imgdata.json') as file:
    data = json.load(file)
file.close()

def display_img(arr):
    im = Image.fromarray(numpy.array(arr))
    im.show()



