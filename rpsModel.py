import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import layers, Sequential, backend
import cv2
from PIL import Image, ImageOps
import os
import sys
import json

# setting up arrays of training data and testing data and stuff

resultKey = {0 : "rock", 1 : "paper", 2 : "scissors"}

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    tf.config.experimental.set_virtual_device_configuration(gpus[0], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])
  except RuntimeError as e:
    print(e)

class model:
    def __init__(self):
        self.model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(50, 50, 1)),
        keras.layers.MaxPooling2D((2, 2), strides=2),
        # second convolution layer
        # keras.layers.Conv2D(64, (3, 3), activation="relu"),
        # keras.layers.MaxPooling2D((2, 2), strides=2),

        # keras.layers.Conv2D(128, (3, 3), activation="relu"),
        # keras.layers.MaxPooling2D((2, 2), strides=2),
        # fully connected classification
        # single vector
        keras.layers.Flatten(),
        keras.layers.Dense(1024, activation="relu"),
        keras.layers.Dense(3, activation=tf.nn.softmax)    # Finds the greatest correlation to one of our labels 1-10
        ])

    def train(self):
        self.train_paths = os.listdir('FaceTrainData/images')
        train_images = []
        train_labels = []
        checkpoint_path = "model/cp.ckpt"
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path, save_weights_only=True, verbose=1)

        for img_path in self.train_paths:
            img = Image.open('FaceTrainData/images/' + img_path)
            train_images.append(np.asarray(img))
        train_images_np = np.asarray(train_images)

        with open('FaceTrainData/labels.json') as file:
            data = json.load(file)
        for label in data.values():
            train_labels.append(label)
        train_labels_np = np.asarray(train_labels)

        self.model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics='accuracy')
        self.model.fit(train_images_np, train_labels_np, epochs=5, callbacks=[cp_callback])
    
    def get_prediction(self, arr):
        print(arr.shape)
        pred_arr = self.model.predict(np.array([arr]))
        prediction = resultKey[np.argmax(pred_arr[0], axis=0)]
        return (prediction, pred_arr)

# train_images = []
# train_labels = []
# test_images = []
# test_labels = []

# train_paths = os.listdir('FaceTrainData/images')
# test_paths = os.listdir('FaceTestData/images')

# for img_path in train_paths:
#     img = Image.open('FaceTrainData/images/' + img_path)
#     train_images.append(np.asarray(img))

# for img_path in test_paths:
#     img = Image.open('FaceTestData/images/' + img_path)
#     test_images.append(np.asarray(img))

# with open('FaceTrainData/labels.json') as file:
#         data = json.load(file)
#         for label in data.values():
#             train_labels.append(label)
        
# train_images_np = np.asarray(train_images)
# train_labels_np = np.asarray(train_labels)
# test_images_np = np.asarray(test_images)
# test_labels_np = np.asarray(train_labels)

# # the model

# model = keras.Sequential([
#     keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(50, 50, 1)),
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

# # code to plug in one image and see what the model thinks it is
# testImage = []

# prediction = model.predict(np.array([testImage]))
# print(prediction)
# pred2 = np.delete(prediction[0], np.array(np.argmax(prediction[0], axis=0)))
# print(f'This is a {result_key[np.argmax(prediction[0], axis=0)]} with a condfidence of {max(prediction[0])} versus the 2nd highest of {max(pred2)}')

# # code to test the model against a bunch of test images

# # test_loss, test_acc = model.evaluate(test_images_np, test_labels_np)
# # print(test_loss, test_acc)