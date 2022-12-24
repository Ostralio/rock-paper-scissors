import json
from PIL import Image
import numpy

# Create in row/column format (2d matrix)
def RC_map(grayscale):
    img = []
    for i in range(0, len(grayscale), 500):
        img.append(grayscale[i:i+500])
    return img

def GS_convert(path):
    with open(path) as file:
        data = json.load(file)
    file.close()

    grayscale = []
    for x in data:
        grayscale.append(0.1*x[0] + 0.6*x[1] + 0.1*x[2])
    
    return RC_map(grayscale)


