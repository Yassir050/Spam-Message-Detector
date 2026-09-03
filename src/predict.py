from pathlib import Path

import joblib


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "spam_model.pkl"


def load_model():
    data = joblib.load(MODEL_PATH)

    return data["model"], data["vectorizer"]


def predict_message(message):
    model, vectorizer = load_model()

    message_vectorized = vectorizer.transform([message])

    prediction = model.predict(message_vectorized)[0]

    return prediction


if __name__ == "__main__":
    message = input("Enter a message: ")

    result = predict_message(message)

    if result == "spam":
        print("🚨 SPAM")
    else:
        print("✅ HAM")
