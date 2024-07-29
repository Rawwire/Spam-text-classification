import streamlit as st
import joblib 
import os
from pathlib import Path


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
model_path = current_dir / "models" / "random_forest_spam_model.pkl"
vectorizer_path = current_dir / "models" / "tfidf_vectorizer.pkl"


rfc = joblib.load(model_path)
tfidf = joblib.load(vectorizer_path)


st.set_page_config(page_title="Spam Text Classification", layout="wide")
st.title("Spam Text Classification")
st.write("This project uses a Random Forest Classifier (Accuracy: 95%) to detect spam messages.")


text_input = st.text_input("Enter the text to be checked:")
if text_input:  
    x_transformed = tfidf.transform([text_input])
    prediction = rfc.predict(x_transformed.toarray())
    st.write("Prediction:", prediction[0])
