import joblib
import os
import sys
from phishing_features import extract_features

def load_trained_model():
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
        model_path = os.path.join(base_path, "models", "best_model.joblib")
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_path, "models", "best_model.joblib")
    return joblib.load(model_path)

def classify(url):
    model = load_trained_model()
    features = extract_features(url)
    prediction = model.predict([features])[0]
    confidence = max(model.predict_proba([features])[0])
    model_name = type(model).__name__
    return prediction, confidence, model_name
