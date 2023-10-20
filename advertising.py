import streamlit as st
import pandas as pd
import pickle

st.write("""
# Sales Prediction App

This app predicts the **Sales Advertising** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 0.500000, 299.000000	, 5.4)
    Radio = st.sidebar.slider('Radio', 0.000000, 49.600000, 4.3)
    Newspaper = st.sidebar.slider('Newspaper', 0.150000, 114.000000, 1.2)
  
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
            
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("advertising.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
