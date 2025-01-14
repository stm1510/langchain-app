import openai
import os
import streamlit as st

# Ensure the OpenAI API key is loaded from environment variables
def load_answer(question):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        return "Error: OpenAI API key is missing. Please check your environment settings."
    
    # Set the OpenAI API key
    openai.api_key = openai_api_key
    
    # Use the new completion API format
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the new model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit App UI setup
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain by Tawfiq - Powered by OpenAI")

# Function to get user input
def get_text():
    input_text = st.text_input("Ask me anything:", key="input")
    return input_text

# Get the user input
user_input = get_text()

# Button to generate the response
submit = st.button('Generate')

# If the 'Generate' button is clicked, display the response
if submit:
    if user_input:
        response = load_answer(user_input)
        st.subheader("Answer:")
        st.write(response)
    else:
        st.warning("Please enter a question to get an answer.")
