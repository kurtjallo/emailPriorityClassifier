import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load the data
data = pd.read_csv("emails.csv")
texts = data["text"]
labels = data["label"]

# Convert text into numbers (TF-IDF)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train a simple classifier
model = LogisticRegression()
model.fit(X, labels)

# Test the model
test_message = ["This is urgent, please call me now"]
test_vector = vectorizer.transform(test_message)
prediction = model.predict(test_vector)

print("Prediction:", prediction[0])

# Save the model and vectorizer for future use
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

