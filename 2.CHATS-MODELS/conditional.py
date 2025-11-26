from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Initialize HuggingFace endpoint
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# Simple parser that outputs plain string
parser = StrOutputParser()

# Prompt template
prompt = PromptTemplate(
    template=(
        "You are an expert sentiment analyzer.\n"
        "Classify the sentiment of the following feedback as strictly one word — 'positive' or 'negative'.\n\n"
        "Feedback: {feedback}\n\n"
        "Answer only 'positive' or 'negative':"
    ),
    input_variables=["feedback"]
)

# Create the chain
chain = prompt | model | parser

# Run
result = chain.invoke({"feedback": "The movie was fantastic! I really loved it."})

# Clean the result (remove extra text if model adds any)
clean_result = result.strip().lower().split()[0]

print(clean_result)
