import streamlit as st
import openai

st.write("**✨ AI GENERATED ARTICLE FROM PUBLISHED PAPER ✨**")

# Get the OpenAI API key from the user
OPENAI_API_KEY = st.text_input("Insert your OpenAI API key here:")
openai.api_key = OPENAI_API_KEY

# Get the info of the paper from the user
name_of_paper = st.text_input("Enter the Title of the paper: ")

# Add a dropdown menu to select the language
languages = ["English", "Español", "Français", "Deutsch", "Italiano","Nederlands"]
language = st.selectbox("Select the language for the output:", languages)

# Define the prompt for the model 
prompt = (f"act as a scientific journalist writing an article for the general public. Summarize the results of the research paper {name_of_paper} and provide numbers to back up the claims in the paper. Lang: {language}")

# Generate text using the GPT-3 model
response = openai.Completion.create(
    engine="text-curie-001",
    prompt=prompt,
    temperature=0.5,
    max_tokens=2048,
    n = 1,
    stop=None,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0,
)

# Print the generated text
st.write(response["choices"][0]["text"])

# End of the app
st.write("**THE END ✨**")
st.write("**Developed by Aster Volta & Ana Cristina Olvera.**")
