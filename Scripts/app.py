#%%
import streamlit as st 
import pandas as pd
import numpy as np 

#%% Page Configuration

st.header("Sales Predictor")

#%% Variables Initialization

model_file = 'sales_predictor_1.sav'

# Number of features
n_features = 3

#%% Users inputs
# Number of features
n_features = 3

# Caption
st.caption("Please enter the following features")

# Inputs columns 
feat_1, feat_2, feat_3 = st.columns(n_features)
# Creations of the inputs 
feat_1_val = feat_1.number_input("Feature 1")
feat_2_val = feat_2.text_input("Feature 2")
feat_3_val = feat_3.selectbox("Feature 3", options=["A","B","C"])


#%% Predictions
''' 
Requirements : 
- sklearn model already trained
- list of features which match with the model features
'''

''' Example to save and load a model

model = LogisticRegression()
model.fit(X_train, Y_train)

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
 
# some time later...
 
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)
'''
loaded_model = pickle.load(open(model_file, 'rb'))
predictions = loaded_model.predict([[feat_1_val, feat_2_val, feat_3_val]])

#%% Display the predictions
st.write("Predictions : ", predictions)