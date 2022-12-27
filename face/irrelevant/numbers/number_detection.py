import tensorflow as tf
import numpy as np
from tensorflow import keras
import PIL 
from PIL import Image, ImageOps
import cv2

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

print(type(train_images))

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)), #input image size 28x28px
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

# # Training machine to identify linear pattern
# model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# model.compile(optimizer='sgd', loss='mean_squared_error')

# xs = np.array([-1, 0, 1, 2, 3, 4], dtype=float) # X input values
# ys = np.array([-3, -1, 1, 3, 5, 7], dtype=float)    # Y input values y = 2x-1

# model.fit(xs, ys, epochs=500)   # Matching xs array values to ys array values, looping 500 times.

# print(model.predict([5, 10])) # Ideal: 9, 19; output: [8.9938135, 18.977531]