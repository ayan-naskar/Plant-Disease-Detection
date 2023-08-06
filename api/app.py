import os
from flask import Flask, request, render_template
import tensorflow as tf
from PIL import Image
import numpy as np
from io import BytesIO
from flask import jsonify
import cv2

app = Flask(__name__)
MODEL = tf.keras.models.load_model("saved_models/10")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

def greenishness(img_array):
    green_pixels = np.sum((img_array[:, :, 1] > img_array[:, :, 0]) & (img_array[:, :, 1] > img_array[:, :, 2]))
    total_pixels = img_array.shape[0] * img_array.shape[1]
    green_proportion = green_pixels / total_pixels
    return green_proportion

def resize_image_opencv_np(image_np, target_size=(256, 256)):
    resized_image = cv2.resize(image_np, target_size, interpolation=cv2.INTER_AREA)
    return resized_image

def classify_image(image):
    image_data = image.read()  # Read the image data as bytes
    img = Image.open(BytesIO(image_data))
    image_np = np.array(img)
    image_np = resize_image_opencv_np(image_np)

    g_ness=greenishness(image_np)
    print("g_ness value=",g_ness)
    if g_ness <= 0.1:
        return {'class': 'Not a Leaf', 'confidence': 1-g_ness}

    img_batch = np.expand_dims(image_np, axis=0)
    predictions = MODEL.predict(img_batch)
    index = np.argmax(predictions[0])
    predicted_class = CLASS_NAMES[index]
    confidence = float(predictions[0][index])
    
    return {'class': predicted_class, 'confidence': confidence}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if 'image' not in request.files:
        return "No image uploaded.", 400

    image = request.files['image']
    if image.filename == '':
        return "No image selected.", 400

    result = classify_image(image)
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
