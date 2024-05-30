import streamlit as st
from langchain_community.llms import OpenAI
from langdetect import detect
from googletrans import Translator

# Initialize translator
translator = Translator()

st.title('🍎🍐🍊 Chat for 남궁만 🥝🍅🍆')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    # Detect the language of the input text
    detected_language = detect(input_text)

    # If the input text is not in English, translate it to English
    if detected_language != 'en':
        input_text = translator.translate(input_text, src=detected_language, dest='en').text

    # Generate response using OpenAI
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    response = llm(input_text)

    # If the detected language is not English, translate the response back to the original language
    if detected_language != 'en':
        response = translator.translate(response, src='en', dest=detected_language).text

    st.info(response)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What do you want?')
    submitted = st.form_submit_button('Submit')

    if not openai_api_key.startswith('sk-'):
        st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')

    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
