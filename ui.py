import pickle
import string
import streamlit as st
import webbrowser



global Lrdetect_Model

LrdetectFile = open('project.pckl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()

st.title("Language Detection tool")
input_test = st.text_input("Provide your input text here",'hello Welcome to from CDAC')

button_clicked = st.button("Get Language Name")
if button_clicked:
	st.text(Lrdetect_Model.predict([input_test]))
