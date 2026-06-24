import streamlit as st
import pickle

st.set_page_config(
    page_title="RakshakAI",
    layout="wide"
)

model = pickle.load(open("../models/scam_model.pkl", "rb"))
vectorizer = pickle.load(open("../models/vectorizer.pkl", "rb"))

st.title("🛡️ RakshakAI")
st.subheader("Digital Arrest Scam Detection System")

message = st.text_area(
    "Enter suspicious message"
)

if st.button("Analyze"):

    x = vectorizer.transform([message])

    prediction = model.predict(x)[0]

    if prediction == 1:
        st.error("🚨 Scam Detected")
    else:
        st.success("✅ Safe Message")