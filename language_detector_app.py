import streamlit as st
import pickle

# Load the saved model
with open('language_detection_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to detect language using the loaded model
def detect_language(text):
    language = model.predict([text])[0]
    return language

# Streamlit UI
st.title('Language Detection App')

# Text input from the user
input_text = st.text_area('Enter the text you want to detect the language of:')

# Button to trigger detection
if st.button('Detect Language'):
    if input_text.strip():
        # Call the detect_language function
        language = detect_language(input_text)
        
        # Display the detected language
        st.write(f'The detected language is: **{language}**')
    else:
        st.write('Please enter some text to detect the language.')
