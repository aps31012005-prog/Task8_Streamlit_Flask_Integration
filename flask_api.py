from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

# ==========================================
# Flask Application
# ==========================================

app = Flask(__name__)


# ==========================================
# CIFAR-10 Class Names
# ==========================================

class_names = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck"
]


# ==========================================
# Load Trained CNN Model
# ==========================================

MODEL_PATH = "model/cifar10_cnn.keras"

print("LOADING CNN MODEL...", flush=True)

model = tf.keras.models.load_model(
    MODEL_PATH,
    compile=False
)

print("CNN MODEL LOADED SUCCESSFULLY", flush=True)


# ==========================================
# Home / Health Check Endpoint
# ==========================================

@app.route("/", methods=["GET"])
def home():

    print("HEALTH CHECK REQUEST RECEIVED", flush=True)

    return jsonify({
        "message": "CIFAR-10 Flask Prediction API is running",
        "endpoint": "/predict",
        "method": "POST"
    })


# ==========================================
# Prediction Endpoint
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    print("PREDICT REQUEST RECEIVED", flush=True)

    if "image" not in request.files:

        print("NO IMAGE PROVIDED", flush=True)

        return jsonify({
            "error": "No image provided. Please upload an image."
        }), 400

    try:

        # ==========================================
        # Receive Image
        # ==========================================

        print("IMAGE RECEIVED", flush=True)

        image_file = request.files["image"]

        # ==========================================
        # Open Image
        # ==========================================

        print("OPENING IMAGE...", flush=True)

        image = Image.open(image_file).convert("RGB")

        print("IMAGE OPENED SUCCESSFULLY", flush=True)

        # ==========================================
        # Resize Image
        # ==========================================

        print("RESIZING IMAGE TO 32x32...", flush=True)

        image = image.resize((32, 32))

        print("IMAGE RESIZED", flush=True)

        # ==========================================
        # Convert to NumPy Array
        # ==========================================

        print("CONVERTING IMAGE TO NUMPY ARRAY...", flush=True)

        image_array = np.array(image)

        print("NUMPY CONVERSION COMPLETED", flush=True)

        # ==========================================
        # Normalize
        # ==========================================

        print("NORMALIZING IMAGE...", flush=True)

        image_array = image_array.astype("float32") / 255.0

        print("IMAGE NORMALIZATION COMPLETED", flush=True)

        # ==========================================
        # Add Batch Dimension
        # ==========================================

        image_array = np.expand_dims(
            image_array,
            axis=0
        )

        print("BATCH DIMENSION ADDED", flush=True)

        # ==========================================
        # Model Prediction
        # ==========================================

        print(
            "IMAGE PREPROCESSING COMPLETE - "
            "STARTING MODEL PREDICTION...",
            flush=True
        )

        predictions = model(
            image_array,
            training=False
        ).numpy()

        print(
            "MODEL PREDICTION COMPLETED SUCCESSFULLY",
            flush=True
        )

        # ==========================================
        # Predicted Class
        # ==========================================

        predicted_index = np.argmax(predictions[0])

        predicted_class = class_names[
            predicted_index
        ]

        print(
            f"PREDICTED CLASS: {predicted_class}",
            flush=True
        )

        # ==========================================
        # Confidence
        # ==========================================

        confidence = float(
            predictions[0][predicted_index]
        ) * 100

        print(
            f"CONFIDENCE: {confidence:.2f}%",
            flush=True
        )

        # ==========================================
        # Return Response
        # ==========================================

        response = {
            "predicted_class": predicted_class,
            "confidence": round(confidence, 2)
        }

        print(
            "SENDING PREDICTION RESPONSE",
            flush=True
        )

        return jsonify(response)

    except Exception as e:

        print(
            f"ERROR DURING PREDICTION: {str(e)}",
            flush=True
        )

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# Run Flask Application
# ==========================================

if __name__ == "__main__":

    print(
        "STARTING FLASK APPLICATION...",
        flush=True
    )

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
