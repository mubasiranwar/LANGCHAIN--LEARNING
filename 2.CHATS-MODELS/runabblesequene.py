from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Hugging Face endpoint
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=200,
    temperature=0.7
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write 5 sentences about the word '{word}'.",
    input_variables=["word"]
)

# ✅ Easiest and most stable method
chain = prompt | model | parser

result = chain.invoke({"word": "happy"})
print(result)
