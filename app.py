import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# download once (safe in Streamlit)
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)

    cleaned = []
    for word in tokens:
        if word.isalnum() and word not in stopwords.words('english') and word not in string.punctuation:
            cleaned.append(ps.stem(word))

    return " ".join(cleaned)


# ===================== LOAD MODEL =====================
model = pickle.load(open("model.pkl", "rb"))


# ===================== UI =====================
st.title("SMS Spam Classifier")

sms = st.text_area("Enter SMS")

if st.button("Predict"):
    if sms.strip() == "":
        st.warning("Please enter a message")
    else:
        transformed_sms = transform_text(sms)

        # IMPORTANT: ONLY predict, no tfidf.transform
        prediction = model.predict([transformed_sms])[0]

        if prediction == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")
