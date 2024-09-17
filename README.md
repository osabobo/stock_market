
# Market Analysis of Stock Price Chatbot

This Streamlit application allows users to analyze stock price data and ask market-related questions. It leverages the `pandasai` library and the `ChatGroq` model for answering questions about stock market data fetched from Yahoo Finance.

## Features

- Fetch stock price data for a given company symbol using Yahoo Finance.
- Use natural language to ask questions about stock price trends and receive detailed, market-savvy responses.
- Powered by the `pandasai` SmartDataframe and the `ChatGroq` LLM for intelligent responses.

## Requirements

Ensure the following Python libraries are installed:

```bash
pip install streamlit pandasai langchain langchain_groq
```

You also need to set up an API key for `PandasAI`. This can be done by setting an environment variable:

```bash
export PANDASAI_API_KEY="your_api_key_here"
```

## How to Use

1. **Run the Streamlit app:**

```bash
streamlit run app.py
```

2. **Enter a company symbol** (e.g., `AAPL` for Apple Inc.) to fetch stock data.

3. **Ask your query**: Type a market-related question (e.g., "What was the highest price for AAPL last month?") and receive an AI-generated response.

## Error Handling

If any errors occur (e.g., invalid company symbol), the app will display an error message.

## Technologies Used

- **Streamlit**: Front-end for displaying the app.
- **PandasAI**: SmartDataframe for querying and analyzing stock market data.
- **LangChain & ChatGroq**: Provides the LLM for answering market analysis questions.

## License

This project is licensed under the MIT License.
