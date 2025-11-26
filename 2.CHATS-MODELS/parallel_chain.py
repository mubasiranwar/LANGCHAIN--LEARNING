from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
# Option 1: From langchain_core (recommended)
from langchain_core.runnables import RunnableSequence



# Option 3: Individual runnable components
from langchain_core.runnables import (
    RunnableParallel,
    RunnableLambda,
    RunnablePassthrough,
    RunnableBranch,
    RunnableMap
)

# Option 4: For creating sequences with the pipe operator
from langchain_core.runnables import Runnable


load_dotenv()

parser=StrOutputParser()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)




prompt1=PromptTemplate(
    template="Make Good notes from the topic in points form:\n\n{topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Genrate 5 question from it:\n\n{topic}",
    input_variables=["topic"]
)

prompt3=PromptTemplate(
    template="Merge the provided quiz and notes\n\n{notes}\n\n{quiz}",
    input_variables=["notes","quiz"]
)



parallel_chain = RunnableParallel({
    'notes': prompt1 | model | parser,
    'quiz': prompt2 | model | parser
})


merge_chain=prompt3 | model | parser
chain=parallel_chain | merge_chain

topic="Human Bones"
result=chain.invoke({"topic":topic})
print(result)
