#%%
import streamlit as st 
import pandas as pd
import numpy as np 

#%% Page Configuration

st.header("Sales Predictor")

#%% Variables Initialization

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
- list of features wich match with the model features
'''
model =
predictions = 