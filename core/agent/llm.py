from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from core.config import config

api_key = config.LLM.get("GEMINI").API_KEY
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=api_key)
print(llm.invoke("Write me a ballad about LangChain"))
