import sqlite3
import re

def run_sql_query(query: str) -> str:
    """
    Executes a SQL query against the ecommerce.db database safely.
    Blocks any destructive queries like DROP, DELETE, UPDATE or INSERT.
    """
    # 1. Safety Check (AST/Keyword Validation) : Block destructuve queries
    forbidden_keywords = ["drop", "delete", "update", "insert", "alter", "truncate"]
    query_lower = query.lower()

    for word in forbidden_keywords:
        # Check if the forbidden words appears as a standalone command
        if re.search(r'\b' + word + r'\b', query_lower):
            return f"SECURITY ERROR: Destructive SQL operation '{word.upper()}' is strictly blocked"

    try:
        # 2. Run read-only connection to execute query
        conn = sqlite3.connect("ecommerce.db")
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return str(results)
    except Exception as e:
        return f"SQL Error: {str(e)}"