# Star Schema Design for FlexiMart Data Warehouse

## Section 1: Schema Overview

### FACT TABLE: fact_sales

**Grain:**  
One row per product per order line item.

**Business Process:**  
Sales transactions capturing product-level purchase details.

**Measures (Numeric Facts):**
- quantity_sold: Number of units sold
- unit_price: Price per unit at time of sale
- discount_amount: Discount applied on the line item
- total_amount: Final amount calculated as (quantity × unit_price − discount)

**Foreign Keys:**
- date_key → dim_date
- product_key → dim_product
- customer_key → dim_customer

---

### DIMENSION TABLE: dim_date

**Purpose:**  
Provides time-based attributes for analyzing sales trends.

**Type:**  
Conformed dimension.

**Attributes:**
- date_key (PK): Surrogate key in YYYYMMDD format
- full_date: Actual calendar date
- day_of_week: Monday, Tuesday, etc.
- day_of_month: Numeric day of month
- month: Month number (1–12)
- month_name: January, February, etc.
- quarter: Q1, Q2, Q3, Q4
- year: Calendar year
- is_weekend: Boolean indicating weekend

---

### DIMENSION TABLE: dim_product

**Purpose:**  
Stores descriptive attributes of products for analysis.

**Attributes:**
- product_key (PK): Surrogate key
- product_id: Business product identifier
- product_name: Name of the product
- category: Product category
- subcategory: Product subcategory
- unit_price: Standard product price

---

### DIMENSION TABLE: dim_customer

**Purpose:**  
Stores customer-related descriptive information.

**Attributes:**
- customer_key (PK): Surrogate key
- customer_id: Business customer identifier
- customer_name: Full name of customer
- city: Customer city
- state: Customer state
- customer_segment: Segment classification (e.g., Retail, Premium)

---

## Section 2: Design Decisions

The fact table uses a transaction line-item level grain to allow detailed analysis of sales at the product level. This granularity enables flexible reporting such as product performance, customer purchasing behavior, and time-based trend analysis.

Surrogate keys are used instead of natural keys to improve performance, maintain historical accuracy, and handle changes in source system identifiers. They also simplify joins and ensure consistency across the data warehouse.

This star schema supports drill-down and roll-up operations effectively. Analysts can roll up data from daily to monthly or yearly levels using the date dimension, and drill down from category-level sales to individual product performance. The simple structure minimizes joins and improves query performance for analytical workloads.

---

## Section 3: Sample Data Flow

**Source Transaction:**  
Order #101, Customer "John Doe", Product "Laptop", Quantity: 2, Unit Price: 50000

**Data Warehouse Representation:**

**fact_sales:**  
{
  date_key: 20240115,
  product_key: 5,
  customer_key: 12,
  quantity_sold: 2,
  unit_price: 50000,
  total_amount: 100000
}

**dim_date:**  
{
  date_key: 20240115,
  full_date: '2024-01-15',
  month: 1,
  quarter: 'Q1'
}

**dim_product:**  
{
  product_key: 5,
  product_name: 'Laptop',
  category: 'Electronics'
}

**dim_customer:**  
{
  customer_key: 12,
  customer_name: 'John Doe',
  city: 'Mumbai'
}
