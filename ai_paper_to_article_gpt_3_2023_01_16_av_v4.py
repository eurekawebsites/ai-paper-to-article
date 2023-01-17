import streamlit as st
import openai

# Get the OpenAI API key from the user
OPENAI_API_KEY = st.text_input("Insert your OpenAI API key here:")
openai.api_key = OPENAI_API_KEY

# Get the name of the article from the user
name_of_article = st.text_input("Nombre del artículo científico: ")

# Define the prompt for the model
prompt = (f"Actúa como periodista y escribe un artículo en español para el público en general. Explica los resultados y proporciona números para respaldar tus afirmaciones. Acerca del artículo titulado {name_of_article}. Lang: es")

# Generate text using the GPT-3 model
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0.3,
    max_tokens=5000,
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
