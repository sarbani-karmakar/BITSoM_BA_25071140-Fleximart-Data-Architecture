# FlexiMart Data Architecture Project

**Student Name:** Sarbani Karmakar
**Student ID:** BITSoM_BA_25071140
**Email:** 30sakarmakar@gmail.com
**Course:** Business Analytics with Gen and Agentic AI
**Date:** Jan 2026

---

## Project Overview

This project implements an end-to-end data architecture solution for **FlexiMart**, a fictional e-commerce company. Acting as a Data Engineer, the goal was to build a complete data pipeline - from raw, dirty CSV files to a fully functional analytics system.

The project covers three major components:
- An **ETL pipeline** that cleans and loads transactional data into a relational MySQL database
- A **NoSQL analysis** comparing RDBMS limitations with MongoDB's flexible document model, with practical MongoDB operations
- A **Data Warehouse** built on a star schema, loaded with realistic data, and queried with OLAP analytics

---

## Marks Breakdown

| Part | Tasks | Marks |
|------|-------|-------|
| Part 1 | ETL Pipeline + Database Schema + Business Queries | 35 |
| Part 2 | NoSQL Analysis (Theory + Practical MongoDB) | 20 |
| Part 3 | Data Warehouse + OLAP Analytics | 35 |
| Documentation | README files and code quality | 10 |
| **Total** | | **100** |

```
## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | ETL pipeline scripting |
| pandas | Data cleaning and transformation |
| mysql-connector-python | Loading data into MySQL |
| MySQL 8.0 | Relational database (fleximart & fleximart_dw) |
| MongoDB | NoSQL document store for product catalog |
| SQL | Business queries and OLAP analytics |
| JavaScript (mongosh) | MongoDB shell operations |

---

## Database Schema (Part 1 — fleximart)

The operational database follows a normalized relational schema in **3NF** with 4 tables:
customers ──< orders ──< order_items >── products

- **customers** — customer profiles (customer_id, name, email, phone, city, registration_date)
- **products** — product catalog (product_id, name, category, price, stock_quantity)
- **orders** — order headers (order_id, customer_id, order_date, total_amount, status)
- **order_items** — line items (order_item_id, order_id, product_id, quantity, unit_price, subtotal)

---

## Data Warehouse Schema (Part 3 — fleximart_dw)

A **star schema** with one fact table and three dimension tables:
dim_date ──┐
dim_product ──── fact_sales
dim_customer ──┘

- **fact_sales** — grain: one row per product per order line item (quantity, unit_price, discount, total_amount)
- **dim_date** — date dimension with day, month, quarter, year, is_weekend
- **dim_product** — product dimension with category and subcategory
- **dim_customer** — customer dimension with city, state, segment

---

## Data Quality Issues Handled (ETL — Part 1)

### customers_raw.csv (25 records)
- Removed **1 duplicate** record (C001 appeared twice)
- Handled **5 missing emails** (C003, C007, C012, C018, C023) — filled with default
- Standardized **inconsistent phone formats** → `+91-XXXXXXXXXX`
- Standardized **inconsistent date formats** → `YYYY-MM-DD`
- Result: **24 unique records loaded**

### products_raw.csv (20 records)
- Handled **3 missing prices** (P003, P010, P017) — filled with category average
- Handled **1 missing stock** (P006) — filled with default value 0
- Standardized **inconsistent category names** → Electronics, Fashion, Groceries
- Result: **20 records loaded**

### sales_raw.csv (40 records)
- Removed **1 duplicate** transaction (T001 appeared twice)
- Dropped **3 records with missing customer_ids** (T004, T016, T030)
- Dropped **2 records with missing product_ids** (T008, T025)
- Standardized **inconsistent date formats** → `YYYY-MM-DD`
- Result: **34 valid records loaded**

---

## Setup Instructions

### Prerequisites
- Python 3.x with `pandas` and `mysql-connector-python`
- MySQL 8.0
- MongoDB with `mongosh`

### Install Python Dependencies
```bash
pip install pandas mysql-connector-python
```

### Database Setup
```bash
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"
```

### Run ETL Pipeline (Part 1)
```bash
python part1-database-etl/etl_pipeline.py
```

### Run Business Queries (Part 1)
```bash
mysql -u root -p fleximart < part1-database-etl/business_queries.sql
```

### Data Warehouse Setup (Part 3)
```bash
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql
```

### MongoDB Setup (Part 2)
```bash
mongosh < part2-nosql/mongodb_operations.js
```

---

## Business Queries Summary (Part 1)

| Query | Business Question | Key Techniques |
|-------|------------------|----------------|
| Query 1 | Customer Purchase History — customers with 2+ orders and >₹5,000 spent | JOIN, GROUP BY, HAVING, aggregate |
| Query 2 | Product Sales Analysis — categories with >₹10,000 revenue | JOIN, GROUP BY, HAVING, COUNT(DISTINCT) |
| Query 3 | Monthly Sales Trend for 2024 with cumulative revenue | SUM() OVER window function, DATE_FORMAT |

---

## OLAP Analytics Summary (Part 3)

| Query | Business Scenario | Key Techniques |
|-------|------------------|----------------|
| Query 1 | Monthly Sales Drill-Down (Year → Quarter → Month) | Star schema join, GROUP BY time dimensions |
| Query 2 | Top 10 Products by Revenue with contribution % | Subquery for percentage calculation, LIMIT |
| Query 3 | Customer Segmentation (High / Medium / Low Value) | CASE WHEN, CTE, GROUP BY segment |

---

## Key Learnings

- Built a complete ETL pipeline handling real-world data quality issues - duplicates, missing values, and format inconsistencies — using Python and pandas
- Designed a normalized relational schema in 3NF and wrote complex multi-table SQL queries with aggregations, window functions, and HAVING clauses
- Compared RDBMS and NoSQL approaches for a product catalog with diverse, schema-flexible data and embedded reviews
- Implemented a star schema data warehouse and understood dimensional modeling concepts like grain, surrogate keys, and drill-down/roll-up operations

---

## Challenges Faced

1. **Mixed date formats across all three CSVs** — solved using `pandas.to_datetime()` with `dayfirst` inference and manual format fallback
2. **Foreign key violations on load** — solved by loading tables in dependency order (customers → products → orders → order_items) and dropping rows with unresolvable foreign keys
3. **Writing cumulative revenue in SQL** — solved using `SUM(monthly_revenue) OVER (ORDER BY month_number ROWS UNBOUNDED PRECEDING)`
4. **MongoDB aggregation pipeline** — understanding `$unwind` on the reviews array to calculate per-product average ratings

---

## Commit History Format
[Part1] Complete ETL pipeline implementation
[Part1] Add schema documentation and business queries
[Part2] Complete NoSQL analysis report
[Part2] Complete MongoDB operations
[Part3] Add star schema design documentation
[Part3] Implement warehouse data and OLAP queries
[Docs]  Update root README

---

## Repository

**GitHub:** `https://github.com/sarbani-karmakar/bitsom_ba_25071140-fleximart-data-architecture`

