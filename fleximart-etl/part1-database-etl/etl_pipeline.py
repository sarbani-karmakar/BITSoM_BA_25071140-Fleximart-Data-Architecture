# ==========================================
# ETL Pipeline for FlexiMart
# Task 1.1 – Data Engineering Assignment
# ==========================================

import pandas as pd
import mysql.connector
from datetime import datetime
# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "$@Rb@n1130",
    "database": "fleximart"
}
try:
    connection = mysql.connector.connect(**db_config)
    print("Connected to MySQL database successfully!")
except mysql.connector.Error as err:
    print("Error:", err)
    
# File paths
customers_file = "Data/customers_raw.csv"
products_file = "Data/products_raw.csv"
sales_file = "Data/sales_raw.csv"

# Extract: Read CSV files
customers_df = pd.read_csv(customers_file)
products_df = pd.read_csv(products_file)
sales_df = pd.read_csv(sales_file)

print("Customers records:", len(customers_df))
print("Products records:", len(products_df))
print("Sales records:", len(sales_df))

# -------------------------------
# Transform: Customers
# -------------------------------

# Track initial customer count
customers_initial = len(customers_df)

# Remove duplicate customers (based on email)
customers_df = customers_df.drop_duplicates(subset="email")
customers_duplicates_removed = customers_initial - len(customers_df)

# Remove rows with missing email
before = len(customers_df)
customers_df = customers_df.dropna(subset=["email"])
customers_missing_emails_removed = before - len(customers_df)

# Clean phone numbers
def clean_phone(phone):
    if pd.isna(phone):
        return None
    digits = "".join(filter(str.isdigit, str(phone)))
    if len(digits) == 10:
        return "+91" + digits
    elif len(digits) == 12 and digits.startswith("91"):
        return "+" + digits
    return None

customers_df["phone"] = customers_df["phone"].apply(clean_phone)

# Standardize city names
customers_df["city"] = customers_df["city"].str.strip().str.title()

# Fix registration_date format
customers_df["registration_date"] = pd.to_datetime(
    customers_df["registration_date"],
    errors="coerce",
    dayfirst=True
).dt.date


# -------------------------------
# Transform: Products
# -------------------------------

# Track initial product count
products_initial = len(products_df)

# Remove products with missing price
before = len(products_df)
products_df = products_df.dropna(subset=["price"])
products_missing_prices_removed = before - len(products_df)

# Fill missing stock with 0
products_df["stock_quantity"] = products_df["stock_quantity"].fillna(0).astype(int)

# Standardize category names
products_df["category"] = products_df["category"].str.strip().str.lower()
products_df["category"] = products_df["category"].replace({
    "electronics": "Electronics",
    "fashion": "Fashion",
    "groceries": "Groceries"
})

# Clean product names (remove extra spaces)
products_df["product_name"] = products_df["product_name"].str.strip()


# -------------------------------
# Transform: Sales
# -------------------------------

# Track initial sales count
sales_initial = len(sales_df)

# Remove duplicate transactions (based on transaction_id)
sales_df = sales_df.drop_duplicates(subset="transaction_id")
sales_duplicates_removed = sales_initial - len(sales_df)

# Remove records with missing customer_id or product_id
before = len(sales_df)
sales_df = sales_df.dropna(subset=["customer_id", "product_id"])
sales_invalid_records_removed = before - len(sales_df)

# Convert transaction_date to YYYY-MM-DD
sales_df["transaction_date"] = pd.to_datetime(
    sales_df["transaction_date"],
    errors="coerce",
    dayfirst=True
).dt.date

# Remove rows where date conversion failed
before = len(sales_df)
sales_df = sales_df.dropna(subset=["transaction_date"])
sales_invalid_records_removed += before - len(sales_df)


# -------------------------------
# Load: Customers
# -------------------------------

cursor = connection.cursor()
# Clear tables before loading (avoid duplicates during reruns)
cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
cursor.execute("TRUNCATE TABLE order_items")
cursor.execute("TRUNCATE TABLE orders")
cursor.execute("TRUNCATE TABLE products")
cursor.execute("TRUNCATE TABLE customers")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
connection.commit()

insert_customer_query = """
INSERT INTO customers (first_name, last_name, email, phone, city, registration_date)
VALUES (%s, %s, %s, %s, %s, %s)
"""

for _, row in customers_df.iterrows():
    cursor.execute(insert_customer_query, (
        row["first_name"],
        row["last_name"],
        row["email"],
        row["phone"],
        row["city"],
        row["registration_date"]
    ))

connection.commit()
print("Customers loaded successfully!")


# -------------------------------
# Load: Products
# -------------------------------

insert_product_query = """
INSERT INTO products (product_name, category, price, stock_quantity)
VALUES (%s, %s, %s, %s)
"""

for _, row in products_df.iterrows():
    cursor.execute(insert_product_query, (
        row["product_name"],
        row["category"],
        row["price"],
        int(row["stock_quantity"])
    ))

connection.commit()
print("Products loaded successfully!")


# -------------------------------
# Load: Orders
# -------------------------------

# Build mapping from customers table
cursor.execute("SELECT customer_id, email FROM customers")
customer_map = {email: customer_id for customer_id, email in cursor.fetchall()}

insert_order_query = """
INSERT INTO orders (customer_id, order_date, total_amount, status)
VALUES (%s, %s, %s, %s)
"""

for _, row in sales_df.iterrows():
    email = row["customer_id"]   # CSV customer_id column contains customer code/email mapping source

    if email not in customer_map:
        continue

    cursor.execute(insert_order_query, (
        customer_map[email],
        row["transaction_date"],
        row["quantity"] * row["unit_price"],
        row["status"]
    ))

connection.commit()
print("Orders loaded successfully!")


# -------------------------------
# Load: Order Items
# -------------------------------

# Build product mapping
cursor.execute("SELECT product_id, product_name FROM products")
product_map = {name: pid for pid, name in cursor.fetchall()}

# Build order mapping
cursor.execute("SELECT order_id, customer_id, order_date FROM orders")
order_rows = cursor.fetchall()

insert_order_item_query = """
INSERT INTO order_items (order_id, product_id, quantity, unit_price, subtotal)
VALUES (%s, %s, %s, %s, %s)
"""

order_index = 0

for _, row in sales_df.iterrows():
    if order_index >= len(order_rows):
        break

    order_id = order_rows[order_index][0]
    product_name = row["product_id"]

    if product_name not in product_map:
        continue

    quantity = row["quantity"]
    price = row["unit_price"]

    cursor.execute(insert_order_item_query, (
        order_id,
        product_map[product_name],
        quantity,
        price,
        quantity * price
    ))

    order_index += 1

connection.commit()
print("Order items loaded successfully!")


# -------------------------------
# Data Quality Report
# -------------------------------

with open("data_quality_report.txt", "w") as f:
    f.write("FlexiMart ETL Data Quality Report\n")
    f.write("---------------------------------\n")
    f.write(f"Customers records processed: {len(customers_df)}\n")
    f.write(f"Products records processed: {len(products_df)}\n")
    f.write(f"Sales records processed: {len(sales_df)}\n")
    f.write("Duplicates handled: Yes\n")
    f.write("Missing values handled: Yes\n")
    f.write("Records loaded successfully into database\n")

print("Data quality report generated!")




