import streamlit as st
import pickle

# ===================== LOAD MODEL =====================
model = pickle.load(open("model.pkl", "rb"))

# ===================== UI =====================
st.title("SMS Spam Classifier")

sms = st.text_area("Enter SMS")

if st.button("Predict"):
    if sms.strip() == "":
        st.warning("Please enter a message")
    else:
        # IMPORTANT: pass RAW text to the pipeline
        prediction = model.predict([sms])[0]

        if prediction == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")


