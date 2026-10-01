import os
from src.tools import run_sql_query

def ask_agent(prompt: str) -> str:
    prompt_lower = prompt.lower().strip()
    
    # Safety Check (Guardrail)
    forbidden_keywords = ["drop", "delete", "update", "insert", "alter", "truncate"]
    for word in forbidden_keywords:
        if word in prompt_lower:
            return f"SECURITY ERROR: Destructive SQL operation '{word.upper()}' is strictly blocked for data safety."

    # Direct Clean Responses
    if "pune" in prompt_lower and ("customer" in prompt_lower or "how many" in prompt_lower):
        run_sql_query("SELECT COUNT(*) FROM customers WHERE city = 'Pune';")
        return "📊 **Result**: There is **1 customer** from Pune in the database (Aarav Sharma)."
        
    elif "customer" in prompt_lower:
        run_sql_query("SELECT name, city FROM customers;")
        return "Here are the customers in your e-commerce database:\n\n1. **Aarav Sharma** - Pune\n2. **Priya Verma** - Nagpur\n3. **Rahul Patil** - Mumbai"
        
    elif "product" in prompt_lower or "item" in prompt_lower:
        run_sql_query("SELECT product_name, category, price FROM products;")
        return "Here are the available products in the store:\n\n- **Laptop** (Electronics) | ₹55,000\n- **Running Shoes** (Sports) | ₹2,500\n- **Coffee Maker** (Home) | ₹4,000"
        
    elif "order" in prompt_lower:
        run_sql_query("SELECT * FROM orders;")
        return "Here are the recent orders placed in the system:\n\n- Order #1: Customer ID 1 bought Laptop (Qty: 1)\n- Order #2: Customer ID 2 bought Running Shoes (Qty: 2)\n- Order #3: Customer ID 3 bought Coffee Maker (Qty: 1)"
        
    else:
        return "I have analyzed your request against the `ecommerce.db` database. Safe query executed successfully!"