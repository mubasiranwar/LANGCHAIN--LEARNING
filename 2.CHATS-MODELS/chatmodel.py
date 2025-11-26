import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set Streamlit page configuration
st.set_page_config(
    page_title="OpenRouter Chat",
    page_icon="🤖",
    layout="centered"
)

# Title and header
st.title("🤖 OpenRouter Chatbot")
st.subheader("Powered by DeepSeek Model via LangChain")

# Input box
user_input = st.text_area("💬 Enter your question:", placeholder="Ask me anything about AI, coding, or the world...")

# Initialize model only once (for performance)
@st.cache_resource
def get_model():
    return ChatOpenAI(
        model="deepseek/deepseek-r1-distill-llama-70b:free",
        base_url="https://openrouter.ai/api/v1",
        temperature=0.7
    )

llm = get_model()

# When user clicks button
if st.button("🚀 Get Answer"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a question first.")
    else:
        with st.spinner("Thinking... 🤔"):
            try:
                response = llm.invoke(user_input)
                st.success("✅ Response:")
                st.write(response.content)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using LangChain + Streamlit + OpenRouter")
