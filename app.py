

import os
import streamlit as st
import google.generativeai as genai

# ==============================
# Configure Gemini
# ==============================
#genai.configure(api_key="GEMINI_API_KEY")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-flash-latest")

# ==============================
# Streamlit Page Settings
# ==============================
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Learning Buddy")
st.write("Learn any topic with the help of Google's Gemini AI.")

# ==============================
# User Input
# ==============================
topic = st.text_input("Enter a Topic")

activity = st.selectbox(
    "Choose an Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

# ==============================
# Generate Response
# ==============================
if st.button("Generate"):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        if activity == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif activity == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif activity == "Generate Quiz":
            prompt = f"Create five multiple-choice questions about {topic} with answers."

        else:
            prompt = topic

        with st.spinner("Generating response..."):

            response = model.generate_content(prompt)

        st.success("Done!")

        st.write(response.text)
