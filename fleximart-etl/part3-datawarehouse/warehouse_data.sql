-- ============================================
-- FlexiMart Data Warehouse Sample Data
-- Database: fleximart_dw
-- ============================================

-- -------------------------
-- dim_date (30 dates: Jan–Feb 2024)
-- -------------------------
INSERT INTO dim_date VALUES
(20240101,'2024-01-01','Monday',1,1,'January','Q1',2024,false),
(20240102,'2024-01-02','Tuesday',2,1,'January','Q1',2024,false),
(20240103,'2024-01-03','Wednesday',3,1,'January','Q1',2024,false),
(20240104,'2024-01-04','Thursday',4,1,'January','Q1',2024,false),
(20240105,'2024-01-05','Friday',5,1,'January','Q1',2024,false),
(20240106,'2024-01-06','Saturday',6,1,'January','Q1',2024,true),
(20240107,'2024-01-07','Sunday',7,1,'January','Q1',2024,true),
(20240110,'2024-01-10','Wednesday',10,1,'January','Q1',2024,false),
(20240115,'2024-01-15','Monday',15,1,'January','Q1',2024,false),
(20240120,'2024-01-20','Saturday',20,1,'January','Q1',2024,true),
(20240125,'2024-01-25','Thursday',25,1,'January','Q1',2024,false),
(20240130,'2024-01-30','Tuesday',30,1,'January','Q1',2024,false),

(20240201,'2024-02-01','Thursday',1,2,'February','Q1',2024,false),
(20240202,'2024-02-02','Friday',2,2,'February','Q1',2024,false),
(20240203,'2024-02-03','Saturday',3,2,'February','Q1',2024,true),
(20240204,'2024-02-04','Sunday',4,2,'February','Q1',2024,true),
(20240205,'2024-02-05','Monday',5,2,'February','Q1',2024,false),
(20240207,'2024-02-07','Wednesday',7,2,'February','Q1',2024,false),
(20240210,'2024-02-10','Saturday',10,2,'February','Q1',2024,true),
(20240214,'2024-02-14','Wednesday',14,2,'February','Q1',2024,false),
(20240215,'2024-02-15','Thursday',15,2,'February','Q1',2024,false),
(20240218,'2024-02-18','Sunday',18,2,'February','Q1',2024,true),
(20240220,'2024-02-20','Tuesday',20,2,'February','Q1',2024,false),
(20240222,'2024-02-22','Thursday',22,2,'February','Q1',2024,false),
(20240224,'2024-02-24','Saturday',24,2,'February','Q1',2024,true),
(20240225,'2024-02-25','Sunday',25,2,'February','Q1',2024,true),
(20240227,'2024-02-27','Tuesday',27,2,'February','Q1',2024,false),
(20240228,'2024-02-28','Wednesday',28,2,'February','Q1',2024,false),
(20240229,'2024-02-29','Thursday',29,2,'February','Q1',2024,false);


-- -------------------------
-- dim_product (15 products, 3 categories)
-- -------------------------
INSERT INTO dim_product (product_id, product_name, category, subcategory, unit_price) VALUES
('P001','Laptop Pro','Electronics','Laptop',75000),
('P002','Smartphone X','Electronics','Mobile',55000),
('P003','Bluetooth Earbuds','Electronics','Accessories',3000),
('P004','LED TV','Electronics','Television',45000),
('P005','Gaming Console','Electronics','Gaming',40000),

('P006','Running Shoes','Fashion','Footwear',5000),
('P007','Jeans','Fashion','Clothing',2500),
('P008','Jacket','Fashion','Clothing',7000),
('P009','Handbag','Fashion','Accessories',9000),
('P010','Sneakers','Fashion','Footwear',6000),

('P011','Office Chair','Furniture','Seating',12000),
('P012','Dining Table','Furniture','Table',45000),
('P013','Bookshelf','Furniture','Storage',8000),
('P014','Sofa','Furniture','Living Room',90000),
('P015','Bed','Furniture','Bedroom',100000);


-- -------------------------
-- dim_customer (12 customers, 4 cities)
-- -------------------------
INSERT INTO dim_customer (customer_id, customer_name, city, state, customer_segment) VALUES
('C001','Rahul Sharma','Mumbai','Maharashtra','High Value'),
('C002','Priya Verma','Delhi','Delhi','Medium Value'),
('C003','Amit Singh','Bangalore','Karnataka','High Value'),
('C004','Neha Gupta','Pune','Maharashtra','Medium Value'),
('C005','Rohan Mehta','Mumbai','Maharashtra','Low Value'),
('C006','Anjali Iyer','Chennai','Tamil Nadu','Medium Value'),
('C007','Karan Patel','Ahmedabad','Gujarat','Low Value'),
('C008','Sneha Rao','Bangalore','Karnataka','High Value'),
('C009','Vikas Malhotra','Delhi','Delhi','Medium Value'),
('C010','Pooja Nair','Kochi','Kerala','Low Value'),
('C011','Arjun Das','Kolkata','West Bengal','Medium Value'),
('C012','Meera Joshi','Pune','Maharashtra','High Value');


-- -------------------------
-- fact_sales (40 transactions)
-- -------------------------
INSERT INTO fact_sales
(date_key, product_key, customer_key, quantity_sold, unit_price, discount_amount, total_amount)
VALUES
(20240101,1,1,1,75000,0,75000),
(20240102,2,2,1,55000,2000,53000),
(20240103,3,3,2,3000,0,6000),
(20240104,4,4,1,45000,3000,42000),
(20240105,5,5,1,40000,0,40000),
(20240106,6,6,2,5000,500,9500),
