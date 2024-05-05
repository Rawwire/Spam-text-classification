import streamlit as st
import joblib 
import os

os.chdir("D:\Projects\Spam text Classifcation")
rfc = joblib.load('models\\random_forest_spam_model.pkl')
tfidf = joblib.load('models\\tfidf_vectorizer.pkl')

st.set_page_config(page_title="Spam Text Classification", layout="wide")
st.title("Spam Text Classification")
st.write("This project uses a Random Forest Classifier (Accuracy: 95%) to detect spam messages.")

text_input = st.text_input("Enter the text to be checked:")
if text_input:  
    x_transformed = tfidf.transform([text_input])
    prediction = rfc.predict(x_transformed.toarray())
    st.write("Prediction:", prediction[0]) 
