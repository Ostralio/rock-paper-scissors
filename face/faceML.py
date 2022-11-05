import tensorflow as tf
import numpy as np
from tensorflow import keras
import PIL 
from PIL import Image, ImageOps
import cv2
import os

def imageFixer(path):
    img = Image.open(path)
    img.thumbnail((28, 28), Image.ANTIALIAS)
    img2 = ImageOps.grayscale(img)
    img_array = np.asarray(img2)
    return img_array

img_array = imageFixer("/Users/siddharth/Desktop/Code/RPS/main/numbers/og9.jpeg")

num_mnist = keras.datasets.mnist

# Images are images, lables are a number corresponding to what the image is.
(train_images, train_labels), (test_images, test_labels) = num_mnist.load_data()
    
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(200, 200)), #input image size 28x28px
    keras.layers.Dense(128, activation=tf.nn.relu),  # we are looking for 128 different "features", throws out data <0
    keras.layers.Dense(10, activation=tf.nn.softmax)    # Finds the greatest correlation to one of our labels 1-10
])

model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_images, train_labels, epochs=5)
# test_loss, test_acc = model.evaluate(test_images, test_labels)
prediction = model.predict(np.array([img_array]))
print(prediction)
pred2 = np.delete(prediction[0], np.array(np.argmax(prediction[0], axis=0)))
print(pred2)
print(f'This is a {np.argmax(prediction[0], axis=0)} with a condfidence of {max(prediction[0])} versus the 2nd highest of {max(pred2)}')