from flask import Flask, render_template, jsonify, request
import joblib
import numpy as np

MODEL_PATH = "model_nam.joblib"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Check if request has a JSON content
    if request.json:
        # Get the JSON as dictionnary
        json_input = request.get_json()
        # Check mandatory key
        if "input" in json_input.keys():
            # Load model
            classifier = joblib.load(MODEL_PATH)
            # Predict
            prediction = classifier.predict(json_input["input"])
            # Return the result as JSON but first we need to transform the
            # result so as to be serializable by jsonify()
            prediction = prediction.tolist()
            # Return prediction
            response = {
                # Since prediction is a float and jsonify function can't handle
                # floats we need to convert it to string
                "prediction": prediction,
            }
            return jsonify(response), 200
    return jsonify({"msg": "Error: not a JSON or no 'input' key in your request"})


if __name__ == "__main__":
    app.run(debug=True)