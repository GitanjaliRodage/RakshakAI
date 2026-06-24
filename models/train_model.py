import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# =========================
# SPAM DATASET
# =========================

spam_df = pd.read_csv("../datasets/spam.csv", encoding="latin-1")

spam_df = spam_df[['v1', 'v2']]
spam_df.columns = ['label', 'text']

spam_df['label'] = spam_df['label'].map({
    'ham': 0,
    'spam': 1
})

# =========================
# PHISHING DATASET
# =========================

phishing_df = pd.read_csv("../datasets/phishing.csv")

phishing_df = phishing_df[['body', 'label']]

phishing_df.columns = ['text', 'label']

# =========================
# DIGITAL ARREST DATASET
# =========================

digital_df = pd.read_csv("../datasets/digital_arrest.csv")

# =========================
# COMBINE ALL DATASETS
# =========================

final_df = pd.concat([
    spam_df[['text', 'label']],
    phishing_df[['text', 'label']],
    digital_df[['text', 'label']]
])

final_df = final_df.dropna()

final_df['text'] = final_df['text'].astype(str)

final_df['label'] = pd.to_numeric(final_df['label'], errors='coerce')

final_df = final_df.dropna()

final_df['label'] = final_df['label'].astype(int)

print(final_df['label'].unique())
print(final_df['label'].dtype)
# =========================
# TRAIN MODEL
# =========================

X = final_df['text']
y = final_df['label']

vectorizer = TfidfVectorizer(max_features=10000)

X_vec = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=1000)
print(phishing_df['label'].unique())
model.fit(X_vec, y)

pickle.dump(model, open("scam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Combined Model Training Complete")
print("Total Records:", len(final_df))