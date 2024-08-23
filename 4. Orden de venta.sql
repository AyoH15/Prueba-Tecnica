SELECT order_id,
	   amount_total,
	   customer_name 
FROM orden_venta
where amount_total > 1000;