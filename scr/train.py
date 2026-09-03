from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from preprocess import load_data, clean_data


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "spam_model.pkl"


def train_model():
    # Load and clean the dataset
    df = load_data()
    df = clean_data(df)

    # Separate messages and labels
    X = df["message"]
    y = df["label"]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Convert text into numerical features
    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )

    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)

    # Create and train the model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vectorized, y_train)

    # Make predictions
    predictions = model.predict(X_test_vectorized)

    # Evaluate the model
    accuracy = accuracy_score(y_test, predictions)

    print("Training completed!")
    print(f"Accuracy: {accuracy:.2%}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    # Save model and vectorizer
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(
        {
            "model": model,
            "vectorizer": vectorizer
        },
        MODEL_PATH
    )

    print(f"\nModel saved to: {MODEL_PATH}")


if __name__ == "__main__":
    train_model()
