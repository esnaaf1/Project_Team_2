#!/usr/bin/env python
# coding: utf-8

# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
from pickle import dump, load
import json
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

# Initialize the flask App
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# Load the model from its pickle file. (This pickle 
# file was originally saved by the code that trained 
# the model. See mlmodel.py)
LogisticRegression = load(open('logisticregression_le.pkl', 'rb'))

# Load the scaler from its pickle file. (This pickle
# file was originally saved by the code that trained 
# the model. See mlmodel.py)
scaler = load(open('scaler_le.pkl','rb'))

# Define the index route
@app.route('/')
def home():
    return render_template('index.html')


# Define a route that runs when the user clicks the Predict button in the web-app
@app.route('/predict',methods=['POST'])
def predict():
    
    # Create a list of the output labels.
    prediction_labels = ['>$50K', '<=$50K']
    
    # Read the list of user-entered values from the website. Note that these
    # will be strings. 
    #features = [x for x in request.form.values()]
    features = json.loads(request.data)
    print(features["age"],features["workclass"],features["degree_type"],features["maritalstatus"],features["occupationType"],features["relationship"],features["race"],
        features["gender"],features["hoursPerWeek"],features["nativecountry"])
    #'age': 39, 'maritalstatus': 'Never-married', 'workclass': 'State-gov', 'race': 'White', 'nativecountry': 'United-States', 
   # 'gender': 'male', 'degree_type': 'Bachelors', 'occupationType': 'Adm-clerical', 'hoursPerWeek': 40}
#input_row1 = [[39, "State-gov", "Bachelors", "Never-married", "Adm-clerical", "Not-in-family", "White", "Male", 40, "United-States"]] # <=50K

    #return str(features)
    value_arr = [[features["age"],features["workclass"],features["degree_type"],features["maritalstatus"],features["occupationType"],features["relationship"],features["race"],
        features["gender"],features["hoursPerWeek"],features["nativecountry"]]]

    input(value_arr)

    # Convert each value to a float.
    #float_features = [float(features[x]) for x in features]

    # Put the list of floats into another list, to make scikit-learn happy. 
    # (This is how scikit-learn wants the data formatted. We touched on this
    # in class.)
    #final_features = [np.array(float_features)]
    #print(final_features)
     
    # Preprocess the input using the ORIGINAL (unpickled) scaler.
    # This scaler was fit to the TRAINING set when we trained the 
    # model, and we must use that same scaler for our prediction 
    # or we won't get accurate results. 
    #final_features_scaled = scaler.transform(final_features)

    # Use the scaled values to make the prediction. 
    #prediction_encoded = LogisticRegression.predict(final_features_scaled)
    #prediction = prediction_labels[prediction_encoded[0]]

    # Render a template that shows the result.
    prediction_text = f'Income level is predicted to be :  {prediction}'
    print(prediction_text)
    return prediction
    #render_template('index.html', prediction_text=prediction_text, features=features)

def input(input_row1):
    #input_row1 = [[39, "State-gov", "Bachelors", "Never-married", "Adm-clerical", "Not-in-family", "White", "Male", 40, "United-States"]] # <=50K
    #input_row2 = [[28, "Private", "Bachelors", "Married-civ-spouse", "Prof-specialty", "Wife", "Black", "Female", 40, "Cuba"]]  # <=50K


    input_row1_df = pd.DataFrame(input_row1, columns=["age", "workclass", "education", "marital-status", "occupation", "relationship",  "race", "sex", "hours-per-week", "native-country"]
    )
    print(input_row1_df)


    # Encode user input
    income_cat = ['workclass',
    'education',
    'marital-status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'native-country']

    # Create a OneHotEncoder instance
    enc = OneHotEncoder(sparse=False)

    # Fit and transform the OneHotEncoder using the categorical variable list
    encode_df = pd.DataFrame(enc.fit_transform(input_row1_df[income_cat]))

    # Add the encoded variable names to the dataframe
    encode_df.columns = enc.get_feature_names_out(income_cat)

    # Merge one-hot encoded features and drop the originals
    input_row1_df = input_row1_df.merge(encode_df, left_index=True, right_index=True).drop(income_cat,1)
    print(input_row1_df)
    # 2. Transform each input using the scaler function.
    input_row1_scaled = scaler.transform(input_row1_df)

    # 3. Make a prediction for each input.
    predict = LogisticRegression.predict(input_row1_scaled)
    answer=predict_labels[predict[0]]
    print(f'Prediction 1 is: {predict_labels[predict[0]]}')
    return answer


# Allow the Flask app to launch from the command line
if __name__ == "__main__":
    app.run(debug=True)