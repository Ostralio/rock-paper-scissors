import tensorflow as tf
import numpy as np
from tensorflow import keras
import PIL 
from PIL import Image, ImageOps

class_names = {0:'T-shirt/top', 1: 'Trouser', 2: 'Pullover', 3: 'Dress', 4: 'Coat',
               5: 'Sandal', 6: 'Shirt', 7: 'Sneaker', 8: 'Bag', 9: 'Ankle boot'}
               
def imageFixer(path):
    img = Image.open(path)
    img.thumbnail((28, 28), Image.ANTIALIAS)
    img2 = ImageOps.grayscale(img)
    return img2

img = imageFixer("/Users/siddharth/Desktop/Code/RPS/main/images.jpg")
img_array = np.asarray(img)

fashion_mnist = keras.datasets.fashion_mnist

# Images are images, lables are a number corresponding to what the image is.
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)), #input image size 28x28px
    keras.layers.Dense(128, activation=tf.nn.relu),  # we are looking for 128 different "features", throws out data <0
    keras.layers.Dense(10, activation=tf.nn.softmax)    # Finds the greatest correlation to one of our labels 1-10
])

model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_images, train_labels, epochs=1)
# test_loss, test_acc = model.evaluate(test_images, test_labels)
prediction = model.predict(np.array([img_array]))
print(prediction)

maxVal = max(prediction[0])
print(maxVal)
print(class_names[np.argmax(prediction[0], axis=0)])

# # Training machine to identify linear pattern
# model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# model.compile(optimizer='sgd', loss='mean_squared_error')

# xs = np.array([-1, 0, 1, 2, 3, 4], dtype=float) # X input values
# ys = np.array([-3, -1, 1, 3, 5, 7], dtype=float)    # Y input values y = 2x-1

# model.fit(xs, ys, epochs=500)   # Matching xs array values to ys array values, looping 500 times.

# print(model.predict([5, 10])) # Ideal: 9, 19; output: [8.9938135, 18.977531]