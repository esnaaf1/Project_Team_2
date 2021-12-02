import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from pickle import dump, load

# Load the dataset
df_income = pd.read_csv("Data/income_evaluation_cleaned.csv")

income_cat = ['workclass',
 'education',
 'marital-status',
 'occupation',
 'relationship',
 'race',
 'sex',
 'native-country']

# Create a OneHotEncoder instance
enc = OneHotEncoder(sparse=False, handle_unknown='ignore')

# Fit and transform the OneHotEncoder using the categorical variable list
encode_df = pd.DataFrame(enc.fit_transform(df_income[income_cat]))

# Add the encoded variable names to the dataframe
encode_df.columns = enc.get_feature_names_out(income_cat)

# Merge one-hot encoded features and drop the originals
#df_income = df_income.merge(encode_df, left_index=True, right_index=True).drop(income_cat,1)
df_income.drop(income_cat,axis=1, inplace=True)
df_income = pd.concat([df_income, encode_df], axis=1)

# Split our preprocessed data into our features and target arrays
X = df_income.drop(columns='income').values
y = df_income['income'].values

print(X)
# Split the preprocessed data into a training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

### Define the scaling function 
# Create a StandardScaler instances
scaler = StandardScaler()

# Fit the StandardScaler
scaler.fit(X_train)

# Transform the training set
X_train_scaled = scaler.transform(X_train)
print(f"Shape of X_train_scaled {X_train_scaled.shape}")



# Define the label encoder and fit it to the training set
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(y_train)

# Transform the labels of the training set
y_train_encoded = le.transform(y_train)

### Define the model
model = LogisticRegression(solver='lbfgs', random_state=1)
model.fit(X_train_scaled, y_train_encoded)

# Save the model to a pickle file (i.e., "pickle it")
# so we can use it from the Flask server. 
dump(model, open('logisticregression_le.pkl', 'wb'))

# Save the scaling function to a pickle file (i.e., "pickle it")
# so we can use it from the Flask server. 
dump(scaler, open('scaler_le.pkl', 'wb'))

# Save the encoding function to a pickle file (i.e., "pickle it")
# so we can use it from the Flask server.
dump(enc, open('enc_le.pkl', 'wb'))


###---------- run to test the model ---------
# Define prediction labels.
predict_labels = ['<=50K','>50K']

# Load the model.
LogisticRegression = load(open('logisticregression_le.pkl', 'rb'))

# Load the scaler.
scaler = load(open('scaler_le.pkl', 'rb'))

# InputData
input_row1 = [[39, "State-gov", "Bachelors", "Never-married", "Adm-clerical", "Not-in-family", "White", "Male", 40, "United-States"]] # <=50K
input_row2 = [[28, "Private", "Bachelors", "Married-civ-spouse", "Prof-specialty", "Wife", "Black", "Female", 40, "Cuba"]]  # <=50K


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
#enc = OneHotEncoder(sparse=False)

# Fit and transform the OneHotEncoder using the categorical variable list
#encode_df = pd.DataFrame(enc.fit_transform(input_row1_df[income_cat]))
encode_df = pd.DataFrame(enc.transform(input_row1_df[income_cat]))

# Add the encoded variable names to the dataframe
encode_df.columns = enc.get_feature_names_out(income_cat)

# Merge one-hot encoded features and drop the originals
#input_row1_df = input_row1_df.merge(encode_df, left_index=True, right_index=True).drop(income_cat,1)
input_row1_df.drop(income_cat,axis=1, inplace=True)
input_row1_df = pd.concat([input_row1_df,encode_df],axis=1)
print(input_row1_df)

# 2. Transform each input using the scaler function.
input_row1_scaled = scaler.fit_transform(input_row1_df)

# 3. Make a prediction for each input.
predict = LogisticRegression.predict(input_row1_scaled)
print(f'Prediction 1 is: {predict_labels[predict[0]]}')