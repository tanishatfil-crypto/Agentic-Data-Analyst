# 📊 Agentic Data Analyst

An intelligent, secure, and interactive data analysis application that allows users to query a local SQLite database (`ecommerce.db`) using natural language. Built with **Python**, **Streamlit**, and **Google Gemini**, this application features a robust security guardrail to prevent unauthorized or destructive database modifications.

---

## 🚀 Key Features

* **Natural Language Queries**: Ask business questions in plain English (e.g., *"How many customers are from Pune?"*) and get instant insights.
* **Security & Safety Guardrails**: A built-in security validation layer detects and blocks unauthorized or destructive SQL operations (such as `DROP`, `DELETE`, `UPDATE`, and `INSERT`).
* **Interactive UI**: A clean, responsive chat interface built using **Streamlit**.
* **Structured E-Commerce Schema**: Pre-configured with relational tables for `customers`, `products`, and `orders`.

---

## 🛠️ Tech Stack

* **Programming Language**: Python
* **Frontend**: Streamlit
* **Database**: SQLite (`ecommerce.db`)
* **AI / LLM Framework**: LangChain & Google Gemini API

---

## 📂 Project Structure

```text
agentic_data_analyst/
│
├── src/
│   ├── agents.py        # Core agent logic and safety checks
│   └── tools.py         # Database connection and secure query execution tool
│
├── ecommerce.db         # SQLite database containing e-commerce data
├── app.py               # Streamlit web application frontend
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

```
## ⚙️ Installation and Setup Guide
Follow these steps to set up and run the project locally on your machine:

### 1. Clone or Open the Project Directory
Open your terminal and navigate to your project folder::
cd C:\Users\YourUsername\agentic_data_analyst

### 2. Install Dependencies

Install all required Python packages using pip:
pip install streamlit langchain langchain-google-genai pydantic

### 3. Configure Your API Key
Ensure your Google Gemini API key is configured or set up in your environment variables.

### 4. Run the Streamlit Application
Start the web application by running the following command in your terminal:
python -m streamlit run app.py
Once running, open the provided local URL (usually http://localhost:8501) in your web browser.
```

```
## 💡 Example Questions You Can Ask
1. "How many customers are from Pune?"

2. "Show me all available products in the store."

3. "List recent orders placed by customers."

4. "Drop the customers table." (Protected by the security guardrail)

## 🛡️ Security Layer Implementation
The application restricts all SQL operations to read-only (SELECT) statements. Any query containing destructive keywords like DROP, ALTER, DELETE, or UPDATE is automatically intercepted and rejected to maintain database integrity.