CREATE TABLE OrderItems_2NF (
  order_id INT,
  line_no INT,
  product_id INT,
  unit_price_at_sale DECIMAL(10,2),  -- historical price
  quantity INT,
  PRIMARY KEY (order_id, line_no),
  FOREIGN KEY (order_id) REFERENCES Orders_2NF(order_id),
  FOREIGN KEY (product_id) REFERENCES Products_2NF(product_id)
);

-- Seed dimension tables (from what we saw in BadOrders/OrderItems_1NF)

INSERT INTO Customers_2NF VALUES

(1, 'Rahul', 'Mumbai'),

(2, 'Priya', 'Delhi');
 
INSERT INTO Products_2NF VALUES

(1, 'Laptop',     'Electronics', 60000),

(2, 'Smartphone', 'Electronics', 30000),

(3, 'Headphones', 'Accessories',  2000);
 
INSERT INTO Orders_2NF VALUES

(101, '2025-09-01', 1),

(102, '2025-09-02', 2);
 
INSERT INTO OrderItems_2NF VALUES

(101, 1, 1, 60000, 1),

(101, 2, 3,  2000, 2),

(102, 1, 2, 30000, 1);
 