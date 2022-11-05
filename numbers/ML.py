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

img_array = imageFixer("/Users/siddharth/Desktop/Code/RPS/main/numbers/briccs/i-tools.png")

folder_paths = os.listdir("/Users/siddharth/Downloads/archive 2/LEGO brick images v1")
train_images = []
train_labels = []
label_key = {'3005 Brick 1x1': 0, '3004 Brick 1x2': 1, '3003 Brick 2x2': 2, '2357 Brick corner 1x2x2': 3}

brick_key = {
    0: "Brick 1x1",
    1: "Brick 1x2",
    2: "Brick 2x2",
    3: "Brick corner 1x2x2",
}

for sub_folder in folder_paths:
    if sub_folder in ['3005 Brick 1x1', '3004 Brick 1x2', '3003 Brick 2x2', '2357 Brick corner 1x2x2']:
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
    keras.layers.Dense(4, activation=tf.nn.softmax)    # Finds the greatest correlation to one of our labels 1-10
])

model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_images_np, train_labels_np, epochs=3)

prediction = model.predict(np.array([img_array]))
print(prediction)
print(f'This is a {brick_key[np.argmax(prediction[0], axis=0)]}')