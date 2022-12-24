import json
from PIL import Image
import numpy

with open('face\website\imgdata.json') as file:
    data = json.load(file)
file.close()

im = Image.fromarray(numpy.array(data))
im.show()



