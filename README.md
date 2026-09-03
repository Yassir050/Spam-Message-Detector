📩 Spam Message Detector

A machine learning project that classifies SMS messages as Spam or Ham (legitimate) using Natural Language Processing (NLP) and supervised machine learning.

The project uses the SMS Spam Collection dataset from the UCI Machine Learning Repository.

✨ Features

* 📩 SMS spam detection
* 📝 Natural Language Processing (NLP)
* 🔤 TF-IDF text vectorization
* 🤖 Logistic Regression classification
* 📊 Model evaluation
* 💾 Model persistence with Joblib
* 🧹 Data cleaning and duplicate removal
* 🛡️ Train/test data splitting

🛠️ Technologies

* Python 3
* Pandas
* Scikit-learn
* Joblib
* Git & GitHub

📊 Dataset

This project uses the SMS Spam Collection dataset from the UCI Machine Learning Repository.

The dataset contains SMS messages labeled as:

* ham — legitimate message
* spam — unwanted message

Dataset source:

UCI Machine Learning Repository — SMS Spam Collection

https://archive.ics.uci.edu/dataset/228/sms%2Bspam%2Bcollection

📁 Project Structure

Spam-Message-Detector/
├── data/
│   └── SMSSpamCollection
│
├── src/
│   ├── preprocess.py
│   └── train.py
│
├── models/
│
├── README.md
├── requirements.txt
└── .gitignore

Files

* SMSSpamCollection — SMS dataset.
* preprocess.py — Loads and cleans the dataset.
* train.py — Trains and evaluates the machine learning model.
* models/ — Stores the trained model locally.
* requirements.txt — Project dependencies.
* .gitignore — Prevents unnecessary files and generated model files from being committed.

⚙️ How It Works

The classification pipeline is:

SMS Message
     ↓
Data Cleaning
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression
     ↓
Spam / Ham

1. Data Loading

The dataset is loaded using Pandas and separated into:

* Message text
* Message label

2. Data Cleaning

Empty rows and duplicate messages are removed before training.

3. Text Vectorization

TF-IDF (Term Frequency–Inverse Document Frequency) converts text into numerical features that can be processed by the machine learning model.

4. Model Training

A Logistic Regression classifier is trained on the vectorized SMS messages.

5. Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score

🚀 Installation

Clone the repository:

git clone https://github.com/Yassir050/Spam-Message-Detector.git

Enter the project directory:

cd Spam-Message-Detector

Install the dependencies:

pip install -r requirements.txt

▶️ Train the Model

Run:

python src/train.py

The program will:

1. Load the dataset.
2. Clean the data.
3. Split the dataset.
4. Convert messages into TF-IDF features.
5. Train the Logistic Regression model.
6. Evaluate the model.
7. Save the trained model locally.

The trained model will be saved as:

models/spam_model.pkl

📈 Example Output

Training completed!
Accuracy: XX.XX%
Classification Report:
              precision    recall    f1-score
ham             ...
spam            ...
Model saved to: models/spam_model.pkl

The exact results may vary depending on the dataset and model configuration.

📚 Skills Practiced

This project demonstrates practical experience with:

* Python
* Pandas
* Data preprocessing
* Natural Language Processing
* TF-IDF
* Text classification
* Logistic Regression
* Train/test splitting
* Model evaluation
* Model persistence
* Git & GitHub

🎯 Project Goal

The goal of this project is to build practical experience in Machine Learning and NLP while developing a clean and organized GitHub project.

This project is part of my learning path toward AI Engineering.

👤 Author

Yassir.B

GitHub:

https://github.com/Yassir050
