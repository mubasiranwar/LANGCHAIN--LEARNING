from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated

class ModelResponse(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment:Annotated[str,"Returen sentiment positive ,negitive or normal"]  # Fixed typo: sentemnet -> sentiment
    value_sentence: Annotated[int,"Return the sentiment review value from 0 to 10 0 for full negative and 10 for full full positive"]  # Changed to lowercase 'int'

load_dotenv()

model = ChatOpenAI(
    model="deepseek/deepseek-r1:free",
    base_url="https://openrouter.ai/api/v1",
    temperature=0.7 
)
structure_output_model = model.with_structured_output(ModelResponse)
response = structure_output_model.invoke("I absolutely love this smartphone! The battery life is incredible - it easily lasts me two full days with moderate use. The camera takes stunning photos, especially in low light conditions. However, the phone is quite heavy and bulky compared to other models, which makes it uncomfortable to hold for long periods. The price is also on the higher side, but for the performance and features you get, I think it's worth it overall.")


print(response['sentiment'])
print(response['value_sentence'])
