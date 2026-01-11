import streamlit as st
import pickle
from llm import generate_reply

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.title("Email Priority Classifier and Reply Generator")

message = st.text_area("Enter the email message:")

if st.button("Classify"):
    vector = vectorizer.transform([message])
    prediction = model.predict(vector)[0]

    str.write("Priority:", prediction)

    if prediction == "urgent":
        reply = generate_reply(message)
        st.subheader("Suggested reply:")
        st.write(reply)