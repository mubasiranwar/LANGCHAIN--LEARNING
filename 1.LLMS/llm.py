from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
llm=OpenAI(temperature=0.7, model_name="gpt-3.5-turbo")

result=llm.invoke("Explain the theory of relativity in simple terms.")
print(result)