Delimiter $$
CREATE PROCEDURE GetTopProducts() 
BEGIN  
	SELECT p.product_name, SUM(od.quantity) AS total_sold,
		sum(od.quantity *p.price) as revenue
	FROM OrderDetails od
    JOIN Products p ON od.Product_id = p.product_id
    Group by p.product_id, p.product_name
    Order by revenue DESC
    LIMIT 3;
 END$$
Delimiter ;
CALL GetTopProducts();