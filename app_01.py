
import streamlit as st
import pickle
import pandas as pd

# Load the Model
with open("new.pkl", "rb") as file:
   loaded_model = pickle.load(file)

# Web App Interface
st.title("Movie Rating Prediction")
st.write("Enter values to predict movie rating ")

# Input Field

Year = st.number_input('Year : ')
Runtime = st.number_input('Runtime in minutes : ')
Votes = st.number_input('No. of votes : ')
Revenue = st.number_input('Revenue in millions : ')
Metascore = st.number_input('Metascore : ')
# Prediction
if st.button("Predict"):
    features = pd.DataFrame([[ Year, Runtime, 
                              Votes, Revenue, Metascore]], 
                            columns=['Year','Runtime (Minutes)','Votes','Revenue (Millions)','Metascore'])
    result = loaded_model.predict(features)
    st.write("Predicted rating:", result[0])
