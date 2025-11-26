from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Gemini model
llm = GoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7)

# Test the model
response = llm.invoke("Explain the theory of relativity in simple terms.")
print(response)
