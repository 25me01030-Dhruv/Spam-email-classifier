import streamlit as st
import pickle
import nltk
import string

from nltk.app.nemo_app import colors
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()  # Lower case
    text = nltk.word_tokenize(text)  # Tokenization text got converted into list here

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)  # Add only alpha numeric characters

    text = y[:]  # y is a list so we can't equate it to another variable directly
    y.clear()

    for j in text:
        if j not in stopwords.words('english') and j not in string.punctuation:
            y.append(j)  # Exclude the punctuations & stopwords

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)  # Return as a string

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Spam Detector')
sms = st.text_area("Write the SMS to verify")

# Preproces
if st.button("Predict") :
    transformed_text = transform_text(sms)
    # vectorize
    vectorized_input = tfidf.transform([transformed_text])
    # Predict
    result = model.predict(vectorized_input)[0]
    # Display
    if result == 0:
        st.subheader(":green[No spam detected]")
    else :
        st.subheader(":red[Spam Detected]")