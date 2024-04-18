# importing dependencies
from dotenv import load_dotenv
load_dotenv() # loading .env variable as environment variables in current session

import os 
from PIL import Image
import streamlit as st
import google.generativeai as genai
from utils import set_background

# configuration with api_key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# func to load GeminiProVision and get response
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(prompt,input_prompt):
    response = model.generate_content([prompt, input_prompt])
    return response.text
# initial streamlit app
st.set_page_config(page_title="Youtube Script Generator")
st.header("Youtube Video Script Generator")

# set background
set_background('background_img.jpg')

# inputs
input_prompt = st.text_input("#### Input Video Title: ",key="input")

# submit button
submit = st.button("Submit")

prompt = """
I will enter a youtube video title and I want you to generate video transcript based on that title.
"""

if submit : 
    response = get_gemini_response(prompt,input_prompt)
    st.subheader("Response: ")
    st.write(response)


                                            