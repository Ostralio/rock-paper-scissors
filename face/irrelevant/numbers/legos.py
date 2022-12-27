import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import layers, Sequential
import cv2
from PIL import Image, ImageOps
import os
import sys

def imageFixer(path):
    img = Image.open(path)
    img.thumbnail((200, 200), Image.ANTIALIAS)
    img2 = ImageOps.grayscale(img)
    img_array = np.asarray(img2)
    return img_array

img_array = imageFixer("/Users/siddharth/Desktop/Code/RPS/main/numbers/briccs/test.png")

folder_paths = os.listdir("/Users/siddharth/Downloads/archive 2/LEGO brick images v1")
train_images = []
train_labels = []
label_key = {'3005 Brick 1x1': 0, '2357 Brick corner 1x2x2': 1, '3024 Plate 1x1': 2, '6632 Technic Lever 3M': 3, '3794 Plate 1X2 with 1 Knob': 4, '3040 Roof Tile 1x2x45deg': 5, '11214 Bush 3M friction with Cross axle': 6, '18651 Cross Axle 2M with Snap friction': 7, '3713 Bush for Cross Axle': 8, '32123 half Bush': 9, '3022 Plate 2x2': 10, '3069 Flat Tile 1x2': 11, '3023 Plate 1x2': 12, '3004 Brick 1x2': 13, '3003 Brick 2x2': 14, '3673 Peg 2M': 15}
brick_key = {
    0: "3005 Brick 1x1",
    1: "2357 Brick corner 1x2x2",
    2: "3024 Plate 1x1",
    3: "6632 Technic Lever 3M",
    4: "3794 Plate 1X2 with 1 Knob",
    5: "3040 Roof Tile 1x2x45deg",
    6: "11214 Bush 3M friction with Cross axle",
    7: "18651 Cross Axle 2M with Snap friction",
    8: "3713 Bush for Cross Axle",
    9: "32123 half Bush",
    10: "3022 Plate 2x2",
    11: "3069 Flat Tile 1x2",
    12: "3023 Plate 1x2",
    13: "3004 Brick 1x2",
    14: "3003 Brick 2x2",
    15: "3673 Peg 2M"
}

for sub_folder in folder_paths:
    if sub_folder != ".DS_Store":
        for img_path in os.listdir(f"/Users/siddharth/Downloads/archive 2/LEGO brick images v1/{sub_folder}"):
            if img_path != ".DS_Store":
                img_obj = Image.open(f"/Users/siddharth/Downloads/archive 2/LEGO brick images v1/{sub_folder}/{img_path}")
                img_obj = ImageOps.grayscale(img_obj)
                train_images.append(np.asarray(img_obj))
                train_labels.append(label_key[sub_folder])

train_images_np = np.asarray(train_images)
train_labels_np = np.asarray(train_labels)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(200, 200)), #input image size 28x28px
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(16, activation=tf.nn.softmax)    # Finds the greatest correlation to one of our labels 1-10
])

model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_images_np, train_labels_np, epochs=5)

prediction = model.predict(np.array([img_array]))
print(prediction)
pred2 = np.delete(prediction[0], np.array(np.argmax(prediction[0], axis=0)))
print(f'This is a {brick_key[np.argmax(prediction[0], axis=0)]} with a condfidence of {max(prediction[0])} versus the 2nd highest of {max(pred2)}')