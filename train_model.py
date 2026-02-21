import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from joblib import dump

from phishing_features import extract_features, get_feature_names

DATA_PATH = "data/urls.csv"
MODEL_PATH = "models/best_model.joblib"

def load_data(path):
    df = pd.read_csv(path)
    df = df.dropna(subset=["url", "label"])
    return df

def build_feature_matrix(urls):
    X = [extract_features(u) for u in urls]
    return np.array(X)

def encode_labels(labels):
    return np.array([1 if str(l).lower() == "phishing" else 0 for l in labels])

def main():
    df = load_data(DATA_PATH)
    urls = df["url"].tolist()
    labels = df["label"].tolist()

    X = build_feature_matrix(urls)
    y = encode_labels(labels)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    print("=== Evaluation on Test Set ===")
    print(f"Accuracy : {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall   : {rec:.4f}")
    print(f"F1-score : {f1:.4f}")

    dump(model, MODEL_PATH)
    print(f"\nModel saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
