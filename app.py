# app.py

"""
Medical Insurance Price Prediction API
Author: Sir Farhan
This API predicts insurance cost based on user inputs.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow access from any phone

@app.route('/predict_price', methods=['POST'])
def predict_price():
    try:
        data = request.json

        # Extract input values
        age = int(data['age'])
        sex = 1 if data['sex'] == 'male' else 0
        bmi = float(data['bmi'])
        children = int(data['children'])
        smoker = 1 if data['smoker'] else 0
        region = data['region']

        # Dummy Formula (Replace with your ML model later)
        base_price = 2500 + (age * 100) + (bmi * 200) + (children * 150)
        if smoker:
            base_price += 5000
        if sex == 1:
            base_price += 500
        if region.lower() == 'southeast':
            base_price += 1000

        return jsonify({'predicted_price': round(base_price, 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
