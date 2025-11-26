from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate



load_dotenv()

parser=StrOutputParser()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)




promt=PromptTemplate(
    template="Summarize the following text in a concise manner:\n\n{text}",
    input_variables=["text"]
)

chain=promt | model | parser
text="LangChain is an open-source framework designed to simplify the development of applications that utilize large language models (LLMs). It provides a modular and flexible architecture that allows developers to easily integrate various components such as LLMs, prompt templates, memory management, and external data sources. With LangChain, developers can create sophisticated applications that leverage the power of LLMs for tasks like natural language understanding, generation, and interaction. The framework supports multiple LLM providers, making it versatile for different use cases and enabling seamless experimentation with different models. Overall, LangChain aims to accelerate the development process and enhance the capabilities of applications built around large language models."

result=chain.invoke({"text":text})  

print(result)