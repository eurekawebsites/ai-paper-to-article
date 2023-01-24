import streamlit as st
import openai

st.write("**✨ AI GENERATED ARTICLE FROM PUBLISHED PAPER ✨**")

# Get the info of the paper from the user
name_paper = st.text_input("Name of paper: ")

# Add a dropdown menu to select the language
languages = ["English", "Español", "Français", "Deutsch", "Italiano","Nederlands"]
language = st.selectbox("Select the language for the output:", languages)

# Get the OpenAI API key from the user
OPENAI_API_KEY = st.text_input("Insert your OpenAI API key here:")
openai.api_key = OPENAI_API_KEY

# Define the prompt for the model 
prompt = (f"What is the overview of the research, findings, implications and recommendations from the paper: {name_paper}. Lang: {language}")

# Generate text using the GPT-3 model
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0.5,
    max_tokens= 4000,
    n = 1,
    stop=None,
)

# Print the generated text
st.write(response["choices"][0]["text"])

# End of the app
st.write("**THE END ✨**")
st.write("**Developed by Aster Volta & Ana Cristina Olvera.**")
