import sqlite3

# 1. Database connection
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# 2. Create Sample tables 
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)
""")

# 3. Dummy data insert karte hain
cursor.executemany("INSERT OR IGNORE INTO customers VALUES (?, ?, ?)", [
    (1, "Aarav Sharma", "Pune"),
    (2, "Priya Verma", "Nagpur"),
    (3, "Rahul Patil", "Mumbai")
])

cursor.executemany("INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?)", [
    (101, "Laptop", "Electronics", 55000.0),
    (102, "Running Shoes", "Sports", 2500.0),
    (103, "Coffee Maker", "Home", 4000.0)
])

cursor.executemany("INSERT OR IGNORE INTO orders VALUES (?, ?, ?, ?, ?)", [
    (1, 1, 101, 1, "2026-01-10"),
    (2, 2, 102, 2, "2026-02-15"),
    (3, 3, 103, 1, "2026-03-01")
])

conn.commit()
conn.close()
print("Database 'ecommerce.db' created and populated successfully!")