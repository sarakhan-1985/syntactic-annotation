
import streamlit as st
import spacy
nlp = spacy.load("en_core_web_sm")
st.write([(word.text, word.pos_) for word in nlp(st.text_input("Enter a sentence"))])
