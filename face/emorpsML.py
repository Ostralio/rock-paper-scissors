import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import layers, Sequential
import cv2
from PIL import Image, ImageOps
import os
import sys
import json

def imageFixer(path):
    img = Image.open(path)
    img.thumbnail((200, 200), Image.ANTIALIAS)
    img2 = ImageOps.grayscale(img)
    img_array = np.asarray(img2)
    return img_array

cv2.imshow("pee pee man", np.array(json.load(open('/Users/siddharth/Desktop/Code/RPS/main/face/website/imgjs.json', 'r'))))

# trainFolderPath = "/Users/siddharth/Downloads/archive3/train"
# testFolderPath = "/Users/siddharth/Downloads/archive3/test"
# train_paths = os.listdir(trainFolderPath)
# test_paths = os.listdir(testFolderPath)
# train_images = []
# train_labels = []
# test_images = []
# test_labels = []
# label_key = {'angry': 0, 'happy': 1, 'disgust': 2, 'fear': 3, 'neutral':4, 'sad':5, 'surprise': 6}
# result_key = {0: 'angry', 1: 'happy', 2: 'disgust', 3: 'fear', 4: 'neutral', 5: 'sad', 6: 'surprise'}

# for sub_folder in train_paths:
#     if sub_folder != ".DS_Store":
#         for img_path in os.listdir(trainFolderPath + "/" + sub_folder):
#             if img_path != ".DS_Store":
#                 img_obj = Image.open(trainFolderPath + "/" + sub_folder + "/" + img_path)
#                 img_obj = ImageOps.grayscale(img_obj)
#                 train_images.append(np.asarray(img_obj))
#                 train_labels.append(label_key[sub_folder])

# for sub_folder in test_paths:
#     if sub_folder != ".DS_Store":
#         for img_path in os.listdir(testFolderPath + "/" + sub_folder):
#             if img_path != ".DS_Store":
#                 img_obj = Image.open(testFolderPath + "/" + sub_folder + "/" + img_path)
#                 img_obj = ImageOps.grayscale(img_obj)
#                 test_images.append(np.asarray(img_obj))
#                 test_labels.append(label_key[sub_folder])

# train_images_np = np.asarray(train_images)
# train_labels_np = np.asarray(train_labels)
# test_images_np = np.asarray(train_images)
# test_labels_np = np.asarray(train_labels)

# model = keras.Sequential([
#     keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(48, 48, 1)),
#     keras.layers.MaxPooling2D((2, 2), strides=2),
#     # second convolution layer
#     keras.layers.Conv2D(64, (3, 3), activation="relu"),
#     keras.layers.MaxPooling2D((2, 2), strides=2),
    
#     # fully connected classification
#     # single vector
#     keras.layers.Flatten(),
#     keras.layers.Dense(1024, activation="relu"),
#     keras.layers.Dense(3, activation=tf.nn.softmax)    # Finds the greatest correlation to one of our labels 1-10
# ])

# model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics='accuracy')
# model.fit(train_images_np, train_labels_np, epochs=5)
# test_loss, test_acc = model.evaluate(test_images_np, test_labels_np)
# print(test_loss, test_acc)

# prediction = model.predict(np.array([img_array]))
# print(prediction)
# pred2 = np.delete(prediction[0], np.array(np.argmax(prediction[0], axis=0)))
# print(f'This is a {result_key[np.argmax(prediction[0], axis=0)]} with a condfidence of {max(prediction[0])} versus the 2nd highest of {max(pred2)}')