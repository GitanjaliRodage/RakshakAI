# RakshakAI

## AI-Powered Digital Public Safety Intelligence Platform

RakshakAI is an AI-based fraud detection platform designed to identify scam messages, phishing attempts, and digital arrest frauds. The system combines Machine Learning, FastAPI, Streamlit, and Geospatial Intelligence to provide a comprehensive public safety solution.

---

## Features

### Scam Detection
- Detects fraudulent SMS and messages.
- Identifies spam and scam content using Machine Learning.

### Phishing Detection
- Detects phishing emails and suspicious messages.
- Trained using phishing datasets.

### Digital Arrest Scam Detection
- Detects messages related to digital arrest scams.
- Flags suspicious government impersonation attempts.

### Crime Intelligence Dashboard
- Interactive geospatial crime map.
- Displays crime hotspots using Folium Maps.

### REST API
- Built using FastAPI.
- Supports integration with external systems.

---

## Tech Stack

- Python
- Scikit-Learn
- Pandas
- FastAPI
- Streamlit
- Folium
- Git & GitHub

---

## Project Structure

```text
RakshakAI
│
├── backend
│   └── main.py
│
├── dashboard
│   ├── dashboard.py
│   └── crime_map.py
│
├── datasets
│   ├── spam.csv
│   ├── phishing.csv
│   └── digital_arrest.csv
│
├── models
│   ├── train_model.py
│   ├── scam_model.pkl
│   └── vectorizer.pkl
│
└── README.md
```

---

## Dataset Information

### SMS Spam Dataset
- 5,574 SMS messages
- Spam and legitimate messages

### Phishing Dataset
- Email phishing dataset
- Used for phishing detection training

### Digital Arrest Dataset
- Custom dataset for digital arrest scam detection

### Total Training Records
- 44,786+ records

---

## Installation

### Clone Repository

```bash
git clone https://github.com/GitanjaliRodage/RakshakAI.git
cd RakshakAI
```

### Install Dependencies

```bash
pip install pandas scikit-learn fastapi uvicorn streamlit folium streamlit-folium
```

---

## Train Model

```bash
cd models
python train_model.py
```

---

## Run Backend

```bash
cd backend
python -m uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000/docs
```

---

## Run Dashboard

```bash
cd dashboard
python -m streamlit run dashboard.py
```

---

## Run Crime Intelligence Map

```bash
cd dashboard
python -m streamlit run crime_map.py
```

---

## Future Enhancements

- Counterfeit Currency Detection
- Voice Scam Detection
- Real-Time Fraud Monitoring
- Cybercrime Analytics Dashboard
- Mobile Application Support

---

## Author

**Gitanjali Rodage**

AI & Data Science Engineer

GitHub:
https://github.com/GitanjaliRodage

---

## License

This project is developed for educational and hackathon purposes.
