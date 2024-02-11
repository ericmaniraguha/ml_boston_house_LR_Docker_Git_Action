import json
import pickle

from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

# Initialize Flask application
app = Flask(__name__)

# Load the trained model and scaler
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for making predictions via API
@app.route('/predict_api', methods=['POST'])
def predict_api():
    # Get the input data from the request
    data = request.json['data']
    
    # Transform the input data using the scaler
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    
    # Make predictions using the trained model
    output = regmodel.predict(new_data)
    
    # Return the prediction as a JSON response
    return jsonify(output[0])

# Route for making predictions via form submission
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    data = [float(x) for x in request.form.values()]
    
    # Transform the input data using the scaler
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    
    # Make predictions using the trained model
    output = regmodel.predict(final_input)[0]
    
    # Render the home template with the prediction result
    return render_template("home.html", prediction_text="The house price prediction is {}".format(output))

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
