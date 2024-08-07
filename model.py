import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
data_file = current_dir / "spam.tsv"
models_dir = current_dir / "models"


models_dir.mkdir(exist_ok=True)


file = pd.read_csv(data_file, sep="\t")
ham = file[file["label"] == "ham"]
spam = file[file["label"] == "spam"]
ham = ham.sample(spam.shape[0])
data = pd.concat([ham, spam], ignore_index=True)


tfidf = TfidfVectorizer()
x = tfidf.fit_transform(data["message"])
x_train, x_test, y_train, y_test = train_test_split(
    x, data["label"], test_size=0.2, random_state=0, stratify=data["label"]
)

rfc = RandomForestClassifier(n_estimators=100, n_jobs=-1)
rfc.fit(x_train, y_train)


joblib.dump(rfc, models_dir / 'random_forest_spam_model.pkl')
joblib.dump(tfidf, models_dir / 'tfidf_vectorizer.pkl')
