from langchain_openai import AzureChatOpenAI  # Updated import
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Streamlit UI
st.title("Charv guy's GPT")

# Initialize LLM
llm = AzureChatOpenAI(
    openai_api_base=os.getenv("AZUREOPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model_name="gpt-4o",
    temperature=0.7
)

# Input and response
user_input = st.text_input("Enter your question:")
if user_input:
    response = llm.invoke(user_input)
    st.write("Response:", response.content)