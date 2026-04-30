# FlexiMart Data Architecture Project

**Student Name:** Sarbani Karmakar  
**Student ID:** bitsom_ba_25071140  
**Email:** 30sakarmakar@gmail.com  
**Date:** December 2025  
---
## Project Overview
This project implements an end-to-end data architecture solution for **FlexiMart**, covering transactional data processing, NoSQL analysis, and data warehousing. It includes an ETL pipeline, business analytics queries, MongoDB-based product catalog analysis, and a star-schema data warehouse with OLAP queries.
---
## Repository Structure
studentID-fleximart-data-architecture/
├── README.md
├── part1-database-etl/
│ ├── etl_pipeline.py
│ ├── schema_documentation.md
│ ├── business_queries.sql
│ ├── data_quality_report.txt
│ └── data/
│ ├── customers_raw.csv
│ ├── products_raw.csv
│ └── sales_raw.csv
├── part2-nosql/
│ ├── nosql_analysis.md
│ ├── mongodb_operations.js
│ └── products_catalog.json
└── part3-datawarehouse/
├── star_schema_design.md
├── warehouse_schema.sql
├── warehouse_data.sql
└── analytics_queries.sql
---
## Technologies Used
- Python 3.x  
- pandas  
- mysql-connector-python  
- MySQL 8.0  
- MongoDB  
- SQL  
- JavaScript (MongoDB Shell)  
---
## Setup Instructions
### Database Setup
```bash
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

Run ETL Pipeline (Part 1)
python part1-database-etl/etl_pipeline.py

Run Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

Data Warehouse Setup (Part 3)
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql

MongoDB Setup (Part 2)
mongosh < part2-nosql/mongodb_operations.js

Key Learnings

Built a complete ETL pipeline with data cleaning, validation, and loading
Designed normalized relational schemas and complex business SQL queries
Compared RDBMS and NoSQL approaches for flexible data modeling
Implemented a star schema and OLAP queries for analytical reporting

Challenges Faced

Handling duplicate and missing records during ETL while maintaining data integrity
Managing foreign key dependencies while loading fact and dimension tables
Writing window functions for cumulative revenue and percentage-based analytics
