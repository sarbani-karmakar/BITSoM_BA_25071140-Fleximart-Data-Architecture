# FlexiMart Database Schema Documentation

## 1. Entity–Relationship Description

### ENTITY: customers
**Purpose:**  
Stores customer-level information required to track purchases and customer activity.

**Attributes:**
- customer_id: Unique identifier for each customer (Primary Key)
- first_name: Customer’s first name
- last_name: Customer’s last name
- email: Customer’s email address (Unique, mandatory)
- phone: Customer’s contact number
- city: City where the customer resides
- registration_date: Date when the customer registered on FlexiMart

**Relationships:**
- One customer can place **many orders**  
  (1:M relationship with the `orders` table)

---

### ENTITY: products
**Purpose:**  
Stores information about products available for sale on FlexiMart.

**Attributes:**
- product_id: Unique identifier for each product (Primary Key)
- product_name: Name of the product
- category: Product category (e.g., Electronics, Fashion)
- price: Price of the product
- stock_quantity: Available inventory quantity

**Relationships:**
- One product can appear in **many order items**  
  (1:M relationship with the `order_items` table)

---

### ENTITY: orders
**Purpose:**  
Stores high-level order information for each customer purchase.

**Attributes:**
- order_id: Unique identifier for each order (Primary Key)
- customer_id: References the customer who placed the order (Foreign Key)
- order_date: Date when the order was placed
- total_amount: Total monetary value of the order
- status: Current order status (Pending, Completed, etc.)

**Relationships:**
- Each order belongs to **one customer**
- Each order can have **many order items**

---

### ENTITY: order_items
**Purpose:**  
Stores detailed line-item information for products included in each order.

**Attributes:**
- order_item_id: Unique identifier for each order item (Primary Key)
- order_id: References the related order (Foreign Key)
- product_id: References the purchased product (Foreign Key)
- quantity: Number of units purchased
- unit_price: Price per unit at time of purchase
- subtotal: Calculated as quantity × unit_price

**Relationships:**
- Many order items belong to **one order**
- Many order items reference **one product**

---

## 2. Normalization Explanation

### a. Third Normal Form (3NF) Justification (≈200–250 words)

The FlexiMart database schema is designed in Third Normal Form (3NF) to ensure data integrity, reduce redundancy, and support efficient updates. Each table represents a single entity type, and all attributes within a table depend solely on the primary key.

In the `customers` table, attributes such as first_name, last_name, email, phone, city, and registration_date depend only on customer_id. No non-key attribute depends on another non-key attribute, ensuring 2NF and 3NF compliance.

The `products` table stores only product-specific attributes. Pricing and stock information are stored once per product, avoiding duplication across orders. This ensures that changes to product price or stock levels require updates in only one place.

The `orders` table separates order-level details from line-item details. Attributes like order_date, total_amount, and status depend only on order_id. Customer information is not duplicated here; instead, a foreign key is used.

The `order_items` table resolves the many-to-many relationship between orders and products. Each non-key attribute (quantity, unit_price, subtotal) depends fully on order_item_id.

### b. Functional Dependencies

- customer_id → first_name, last_name, email, phone, city, registration_date
- product_id → product_name, category, price, stock_quantity
- order_id → customer_id, order_date, total_amount, status
- order_item_id → order_id, product_id, quantity, unit_price, subtotal

### c. Avoidance of Anomalies

- **Update anomaly:** Changes to customer or product information are made in one place only.
- **Insert anomaly:** New customers, products, or orders can be added independently.
- **Delete anomaly:** Deleting an order does not remove customer or product data.

---

## 3. Sample Data Representation

### customers (Sample Records)

| customer_id | first_name | last_name | email                    | city     |
|------------|------------|-----------|--------------------------|----------|
| 1          | Rahul      | Sharma    | rahul.sharma@gmail.com   | Mumbai   |
| 2          | Priya      | Verma     | priya.verma@gmail.com    | Delhi    |

---

### products (Sample Records)

| product_id | product_name         | category     | price   |
|-----------|----------------------|--------------|---------|
| 1         | Samsung Galaxy S21   | Electronics  | 45999   |
| 2         | Nike Running Shoes   | Fashion      | 3499    |

---

### orders (Sample Records)

| order_id | customer_id | order_date | total_amount |
|---------|-------------|------------|--------------|
| 1       | 1           | 2024-06-15 | 45999        |
| 2       | 2           | 2024-06-16 | 3499         |

---

### order_items (Sample Records)

| order_item_id | order_id | product_id | quantity | subtotal |
|--------------|----------|------------|----------|----------|
| 1            | 1        | 1          | 1        | 45999    |
| 2            | 2        | 2          | 1        | 3499     |
