# NoSQL Database Analysis for FlexiMart

## Section A: Limitations of Relational Databases (RDBMS)

Relational databases like MySQL work well when data is highly structured and consistent, but they struggle when dealing with highly diverse product data. In FlexiMart’s case, different product types have different attributes. For example, laptops require specifications such as RAM, processor, and storage, while shoes require size, color, and material. In a relational model, this would require multiple additional tables or many nullable columns, leading to complexity and inefficiency.

Frequent schema changes are another limitation. Each time FlexiMart adds a new product category with unique attributes, the database schema must be altered. Schema changes in relational databases are expensive, risky in production systems, and can cause downtime.

Storing customer reviews is also problematic in RDBMS. Reviews naturally form a nested structure under products, but relational databases require separate tables and complex joins to retrieve reviews. This increases query complexity and impacts performance, especially when the number of reviews grows.

---

## Section B: Benefits of MongoDB (NoSQL)

MongoDB solves these issues by using a flexible, document-based schema. Each product can store its own structure, allowing laptops, shoes, and electronics to coexist in the same collection without schema changes. New attributes can be added to products without modifying existing documents or impacting other product types.

MongoDB supports embedded documents, making it ideal for storing customer reviews directly inside the product document. This allows faster reads, simpler queries, and better alignment with real-world data structures.

MongoDB is also designed for horizontal scalability. As FlexiMart’s product catalog grows, MongoDB can scale across multiple servers using sharding. This makes it suitable for handling large volumes of product data and high traffic without sacrificing performance.

---

## Section C: Trade-offs of Using MongoDB

One disadvantage of MongoDB is weaker support for complex transactions compared to MySQL. While MongoDB supports transactions, relational databases handle multi-table transactions more naturally.

Another drawback is data consistency. MongoDB follows a more flexible consistency model, which may lead to data duplication or inconsistency if not carefully designed. This requires developers to enforce data integrity at the application level rather than relying entirely on the database.
