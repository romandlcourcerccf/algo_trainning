-- Write your PostgreSQL query statement below
select Product.product_name as product_name, Sales.year as year, Sales.price as price
from Product join Sales 
on Product.product_id = Sales.product_id