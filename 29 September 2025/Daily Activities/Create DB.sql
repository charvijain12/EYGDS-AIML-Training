CREATE DATABASE RetailDB;
USE RetailDB;

CREATE TABLE Customers(
	customer_id INT auto_increment PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50),
    phone VARCHAR(15)
);

CREATE TABLE Products (
	product_id INT auto_increment PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE Orders(
	order_id INT auto_increment PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
CREATE TABLE OrderDetails (
	order_detail_id INT auto_increment PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
	