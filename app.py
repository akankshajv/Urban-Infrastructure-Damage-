from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from PIL import Image
import os

app = Flask(__name__)

# ---- LOAD MODEL HERE ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "hurricane_damage_model.keras")

print("Loading model from:", model_path)

model = tf.keras.models.load_model(model_path)
# -------------------------

def preprocess(img):
    img = img.resize((224,224))
    img = np.array(img)/255.0
    img = np.expand_dims(img,axis=0)
    return img


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    file = request.files['image']
    img = Image.open(file)

    processed = preprocess(img)

    prediction = model.predict(processed)

    confidence = float(prediction[0][0]) * 100

    if prediction[0][0] > 0.5:
        result = "Intact"
    else:
        result = "At risk"

    return render_template("result.html",
                           prediction=result,
                           confidence=round(confidence,2))

if __name__ == "__main__":
    app.run(debug=True)