from fastapi import FastAPI
import pickle

app = FastAPI()

model = pickle.load(open("../models/scam_model.pkl", "rb"))
vectorizer = pickle.load(open("../models/vectorizer.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "RakshakAI Running"}

@app.get("/detect")
def detect(text: str):

    x = vectorizer.transform([text])

    prediction = model.predict(x)[0]

    if prediction == 1:
        return {"result": "Scam Detected"}

    return {"result": "Safe"}