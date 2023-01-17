import streamlit as st
import openai

st.write("**✨ AI GENERATED ARTICLE FROM PUBLISHED PAPER ✨**")

# Get the OpenAI API key from the user
OPENAI_API_KEY = st.text_input("Insert your OpenAI API key here:")
openai.api_key = OPENAI_API_KEY

# Get the DOI of the article from the user
doi_of_article = st.text_input("Enter the DOI of the article: ")

# Add a dropdown menu to select the language
languages = ["English", "Español", "Français", "Deutsch", "Italiano","Nederlands","Ελληνικά","日本語","中文","Русский","Português","Polski","Svenska"]
language = st.selectbox("Select the language for the output:", languages)

# Define the prompt for the model 
prompt = (f"act as a scientific journalist and write an article for the general public. Explain the results and provide numbers to back up their claims. About the article with DOI: {doi_of_article}. Lang: {language}")

# Generate text using the GPT-3 model
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0.3,
    max_tokens=4030,
    n = 1,
    stop=None,
    top_p = 1,
    frequency_penalty = 1,
    presence_penalty = 0,
)

# Print the generated text
st.write(response["choices"][0]["text"])

# End of the app
st.write("**THE END ✨**")
st.write("**Developed by Aster Volta & Ana Cristina Olvera.**")
