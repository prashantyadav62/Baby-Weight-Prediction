import pandas as pd
import pickle
import os
from flask import Blueprint, request, jsonify
from extentions import cache


base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
path = os.path.join(base_dir, "model.pkl")

# Load ML model
with open(path, 'rb') as obj:
    model = pickle.load(obj)


predict_bp = Blueprint("predict", __name__)

EXPECTED_COLUMNS = ['gestation', 'parity', 'age', 'height', 'weight', 'smoke']

def get_cleaned_data(form_data):
    gestation = float(form_data['gestation'])
    parity = int(form_data['parity'])
    age = float(form_data['age'])
    height = float(form_data['height'])
    weight = float(form_data['weight'])
    smoke = float(form_data['smoke'])

    cleaned_Data = {
        "gestation": [gestation],
        "parity": [parity],
        "age": [age],
        "height": [height],
        "weight": [weight],
        "smoke": [smoke]
    }
    return cleaned_Data


    


##define the endpoint
@predict_bp.route("/predict", methods = ["POST"])
@cache.cached(timeout=30, query_string=True)  # Cache the response for 60 seconds
def get_prediction():
    #get data from user
    # baby_data_form = request.form
    baby_data_form = request.get_json()

    # baby_data_cleaned = get_cleaned_data(baby_data_form)

    #convert data into dataframe
    baby_df = pd.DataFrame(baby_data_form)
    baby_df = baby_df[EXPECTED_COLUMNS]

    # base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # path = os.path.join(base_dir, "model.pkl")

    # if not os.path.exists(path):
    #     return jsonify({"error": f"Model file not found at {path}"}), 404

    # # Load ML model
    # with open(path, 'rb') as obj:
    #     model = pickle.load(obj)

    #make prediction on user data
    prediction = model.predict(baby_df)

    prediction = round(float(prediction), 2)

    #return reponse in a json format
    response = {"Prediction": prediction}

    # return render_template("index.html", prediction = prediction)
    return response