from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask application
app = Flask(__name__)

# Load the trained ML model from the .pkl file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the prediction route
@app.route('/predict_price', methods=['POST'])
def predict_price():
    try:
        # Get the input data from the request body (in JSON format)
        data = request.get_json()

        # Extract the input data (age, sex, bmi, children, smoker, region)
        age = data['age']
        sex = data['sex']  # Ensure 'sex' is encoded as 0 for male, 1 for female
        bmi = data['bmi']
        children = data['children']
        smoker = data['smoker']  # 0 = non-smoker, 1 = smoker
        region = data['region']  # 0 = northeast, 1 = southeast, 2 = southwest, 3 = northwest

        # Prepare the input data as a numpy array (the model expects it in this format)
        input_data = np.array([[age, sex, bmi, children, smoker, region]])

        # Make the prediction using the model
        predicted_price = model.predict(input_data)

        # Return the predicted price as a JSON response
        return jsonify({'predicted_price': predicted_price[0]})

    except Exception as e:
        # In case of an error, return a 500 status code and error message
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
