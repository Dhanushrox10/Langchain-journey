import sqlite3

conn = sqlite3.connect("SalesDB/sales.db")
cursor = conn.cursor()

# Delete table completely for ID to start from 1 again
cursor.execute("DROP TABLE IF EXISTS orders")

# Create table again to avoid duplicate entries when running the script multiple times 
cursor.execute("""
CREATE TABLE orders (
id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_name TEXT NOT NULL,
product_name TEXT NOT NULL,
quantity INTEGER NOT NULL,
price REAL NOT NULL,
total REAL NOT NULL
)
""")

# Insert data
cursor.execute("""
INSERT INTO orders (customer_name, product_name, quantity, price, total) VALUES
("John Doe", "Laptop", 1, 1000.00, 1000.00),
("Jane Smith", "Smartphone", 2, 500.00, 1000.00),
("Bob Johnson", "Tablet", 3, 200.00, 600.00)
""")

conn.commit()
conn.close()