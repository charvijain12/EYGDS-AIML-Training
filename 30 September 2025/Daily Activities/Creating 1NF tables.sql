
INSERT INTO Orders_1NF (order_id, order_date, customer_id, customer_name, customer_city)
VALUES (101, '2025-09-01',1,'Alice','Delhi'),
	    (102, '2025-09-02','Bob','Mumbai');


INSERT INTO OrderItems_1NF VALUES
(101, 1, 1, 'Laptop',    60000, 1),
(101, 2, 3, 'Headphones', 2000, 2);

INSERT INTO OrderItems_1NF VALUES
(102, 1, 2, 'Smartphone', 30000, 1);

