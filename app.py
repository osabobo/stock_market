import streamlit as st
from pandasai import SmartDataframe
from pandasai.connectors.yahoo_finance import YahooFinanceConnector
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
# Set your PandasAI API key
#os.environ['PANDASAI_API_KEY'] = "$2a$10$ejBcbjF2sOx4XaiHsGqMxOTutW/iu54/RpYefPHF8je7Vxz.BEHnq"
# Initialize the ChatGroq model
#groq_api_key = st.secrets["GROQ_API_KEY"]

groq_api_key = os.getenv("GROQ_API_KEY")  # ✅ Correct

if not groq_api_key:
    st.error("GROQ_API_KEY is not set. Please add it as an environment variable.")
else:
    model = ChatGroq(
        temperature=0.2,
        model="llama-3.3-70b-versatile",
        groq_api_key=groq_api_key
    )

#model = ChatGroq(temperature=0.8, model="llama-3.3-70b-versatile",groq_api_key=groq_api_key)
# Streamlit app
st.title("Market Analysis of Stock Price Chatbot")
#Create a prompt template
prompt = ChatPromptTemplate.from_messages([
("system", ""You are a highly skilled Market Analyst with expertise in historical and current market trends. Your responses should be:

Data-driven, with accurate statistics, dates, and sources where applicable

Structured logically (e.g., cause-effect, chronological, or comparative analysis)

Clear and concise, avoiding unnecessary jargon unless explained

Focused on key insights, not just general observations

Adapted to the context (e.g., specify if the question relates to stocks, commodities, crypto, etc.)

If data is uncertain or speculative, acknowledge limitations transparently. Prioritize the most relevant historical patterns, economic conditions, and geopolitical factors influencing the market event in question."."),
("human", "{question}")
])
# Text input for the company symbol
company_symbol = st.text_input("Enter the company symbol (e.g., AAPL):")

if company_symbol:
    try:
        # Initialize the Yahoo Finance connector with the input symbol
        yahoo_connector = YahooFinanceConnector(company_symbol)
        df = SmartDataframe(yahoo_connector, config={"llm": model},description=prompt)

        # Text input for user queries
        user_query = st.chat_input("Ask a question about the market:")

        if user_query:
            # Get the chatbot's response
            response = df.chat(user_query)
            st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
