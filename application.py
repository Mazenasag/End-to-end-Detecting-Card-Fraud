from flask import Flask, request, jsonify,render_template
from src.CardFraud.pipeline.predict import PredictionPipeline
from pathlib import Path


app = Flask(__name__)

# Load pipeline
pipeline = PredictionPipeline(Path("artifacts/model.pkl"), Path("artifacts/scaler.pkl"))

@app.route('/')
def home():
    return render_template('index.html')  # Render input form

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_string = request.form['input_data']  # Get string input from form
        input_list = list(map(float, input_string.strip().split(',')))  # Convert to float list

        if len(input_list) != 29:
            return "Error: You must enter exactly 29 comma-separated values."

        prediction  = pipeline.predict(input_list)
        result = "Fraud" if prediction == 1 else "Not Fraud"
        return render_template('index.html', prediction_text=f"Prediction: {result}")

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
