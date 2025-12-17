import streamlit as st
import pickle
model = pickle.load(open("model.pkl", "rb"))
st.title("SMS Spam Classifier")

sms = st.text_area("Enter SMS")

if st.button("Predict"):
    if sms.strip() == "":
        st.warning("Please enter a message")
    else:
        prediction = model.predict([sms])[0]

        if prediction == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")
