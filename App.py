import streamlit as st
import pickle
with open('vectorizer.pkl', 'rb') as file:
    tfidf = pickle.load(file)

mnb = pickle.load(open('model.pkl', 'rb'))
st.title("Email spam detection")

input_email = st.text_input("Enter email/sms")
if st.button('Predict'):
    vector_input = tfidf.transform([input_email])  # Convert input_email to a list with a single element
    result = mnb.predict(vector_input)
    if result == 1:
     st.header("Spam")
    else:
     st.header("Ham")

