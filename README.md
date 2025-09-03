LangChain and LangGraph Demo
=======================

This repository contains Jupyter Notebooks (.ipynb) showcasing the basics of working with **LangChain** and **LangGraph**, including how to connect it with OpenAI, LangSmith, and Tavily APIs.

📦 Setup & Installation
-----------------------

Clone this repository and install the dependencies:

`  pip install -r requirements.txt  `

🔑 Environment Variables
------------------------

Before running the notebook, create a .env file in the project root with the following keys:

<code>OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=langchain-demo
TAVILY_API_KEY=your_tavily_api_key </code>

### Where to get these keys:

*   OpenAI API Key → [Create API key](https://platform.openai.com/api-keys)

    ⚠️ You need to have an active balance to start using OpenAI.
    
*   **LangSmith API Key** → [Create account & API key](https://docs.langchain.com/langsmith/create-account-api-key?utm_source=chatgpt.com) Add this to LANGCHAIN\_API\_KEY.

    Set LANGCHAIN\_PROJECT to any project name you like (e.g., langchain-demo).
    
*   **Tavily API Key** → [Sign up here](https://www.tavily.com/?utm_source=chatgpt.com)
    

▶️ Running the Notebook
-----------------------

### Option 1: Jupyter Notebook

` jupyter notebook `

Open the .ipynb file and run the cells step by step. 🚀

### Option 2: VS Code

You can also run the notebook directly inside **Visual Studio Code**:

1.  Install [Visual Studio Code](https://code.visualstudio.com/?utm_source=chatgpt.com).
    
2.  Install the **Python** and **Jupyter** extensions from the Extensions Marketplace.
    
3.  Open this repository folder in VS Code.
    
4.  Open the .ipynb file.
    
5.  Select a Python interpreter with the dependencies installed (pip install -r requirements.txt).
    
6.  Run the notebook cells using the ▶️ icons in the editor.
    

👉 Detailed guide: [Using Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks?utm_source=chatgpt.com)

📚 About
--------

This demo is designed for introducing LangChain and LangGraph. It walks through key concepts such as:

*   Using LangChain with OpenAI models
    
*   Tracking experiments with LangSmith
    
*   Adding external tools like Tavily for search