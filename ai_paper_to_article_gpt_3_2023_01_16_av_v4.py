import streamlit as st
import openai

st.write("**✨ AI GENERATED ARTICLE FROM PUBLISHED PAPER ✨**")

# Get the OpenAI API key from the user
OPENAI_API_KEY = st.text_input("Insert your OpenAI API key here:")
openai.api_key = OPENAI_API_KEY

# Get the name of the article, and first author, from the user
name_of_article = st.text_input("Nombre del artículo científico: ")
name_of_author = st.text_input("Nombre del primer autor: ")

# Define the prompt for the model
prompt = (f"act as a scientific journalist and write an article in Spanish for the general public. Explain the results and provide numbers to back up their claims. About the scientific paper {name_of_article} by {name_of_author}. Lang: es")

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
