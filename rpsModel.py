import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import layers, Sequential
import cv2
from PIL import Image, ImageOps
import os
import sys
import json

train_images = []
train_labels = []
test_images = []
test_labels = []

label_key = {'rock': 0, 'scissors': 1, 'paper': 2}
result_key = {0: 'rock', 1: 'scissors', 2: 'paper'}

train_paths = os.listdir('FaceTrainData/images')
test_paths = os.listdir('FaceTestData/images')

for img_path in train_paths:
    img = Image.open('FaceTrainData/images/' + img_path)
    train_images.append(np.asarray(img))

for img_path in test_paths:
    img = Image.open('FaceTestData/images/' + img_path)
    test_images.append(np.asarray(img))

with open('FaceTrainData/labels.json') as file:
        data = json.load(file)
        

train_images_np = np.asarray(train_images)
train_labels_np = np.asarray(train_labels)
test_images_np = np.asarray(test_images)
test_labels_np = np.asarray(train_labels)

# model = keras.Sequential([
#     keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(48, 48, 1)),
#     keras.layers.MaxPooling2D((2, 2), strides=2),
#     # second convolution layer
#     keras.layers.Conv2D(64, (3, 3), activation="relu"),
#     keras.layers.MaxPooling2D((2, 2), strides=2),

#     keras.layers.Conv2D(128, (3, 3), activation="relu"),
#     keras.layers.MaxPooling2D((2, 2), strides=2),
#     # fully connected classification
#     # single vector
#     keras.layers.Flatten(),
#     keras.layers.Dense(1024, activation="relu"),
#     keras.layers.Dense(7, activation=tf.nn.softmax)    # Finds the greatest correlation to one of our labels 1-10
# ])

# model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics='accuracy')
# model.fit(train_images_np, train_labels_np, epochs=5)
# test_loss, test_acc = model.evaluate(test_images_np, test_labels_np)
# print(test_loss, test_acc)

