from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()

st.set_page_config(page_title="Gemini Image & Text Q&A", page_icon="🤖", layout="centered", initial_sidebar_state="collapsed")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.title("🌟 Gemini AI Image & Text Q&A")
st.markdown("""
    <style>
        .main-header { font-size: 24px; font-weight: bold; color: #4B9CD3; }
        .instructions { font-size: 16px; color: #555555; margin-bottom: 15px; }
        .response-box { border: 1px solid #4B9CD3; padding: 15px; border-radius: 10px; background-color: #f0f8ff; }
        .prompt-label { font-weight: bold; color: #4B9CD3; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="instructions">Upload an image and type a question to get a response from the Gemini AI model. The model will analyze the image and provide insights or answer your queries based on both the input prompt and the image.</p>', unsafe_allow_html=True)

input_text = st.text_input("🔍 Input your question or prompt:", key="input")

uploaded_file = st.file_uploader("📂 Choose an image (jpg, jpeg, png):", type=["jpg", "jpeg", "png"])
image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image Preview", use_column_width=True)

submit = st.button("🚀 Generate Response")

if submit:
    if uploaded_file is None:
        st.error("Please upload an image.")
    else:
        with st.spinner("Analyzing..."):
            response = get_gemini_response(input_text, image)
        st.subheader("🤖 AI Response")
        st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)

# Footer with additional info or instructions
st.markdown("""
    ---
    **Gemini AI Q&A App**  
    Powered by [Google Gemini](https://ai.google). This demo allows you to ask questions based on image input and prompts. Explore the power of vision + language models!
""")
