import os
import base64
import re
from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from io import BytesIO

# Initialize the Flask application
app = Flask(__name__, template_folder='templates')

# Load the trained model
try:
    model = keras.models.load_model("mnist_model.h5")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    """Renders the main page of the application."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles the image data from the canvas and makes a prediction.
    """
    if model is None:
        return jsonify({'error': 'Model not loaded. Please train the model first.'}), 500

    data = request.json
    if 'image_data' not in data:
        return jsonify({'error': 'No image data received'}), 400

    image_data = data['image_data']

    try:
        # Extract base64 part and decode
        img_string = re.search(r'base64,(.*)', image_data).group(1)
        image_bytes = base64.b64decode(img_string)

        # Open and preprocess the image
        image = Image.open(BytesIO(image_bytes)).convert('L')
        image = image.resize((28, 28))
        img_array = np.array(image)

        # Invert colors and normalize
        img_array = img_array.astype("float32")
        img_array = 255.0 - img_array
        img_array /= 255.0

        # Reshape the image for the model
        img_array = np.expand_dims(img_array, axis=0)
        img_array = np.expand_dims(img_array, axis=-1)

        # Make a prediction
        prediction = model.predict(img_array)
        predicted_class = int(np.argmax(prediction, axis=1)[0])
        confidence = float(np.max(prediction) * 100)

        return jsonify({
            'prediction': predicted_class,
            'confidence': f'{confidence:.2f}%'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, port=5000)
