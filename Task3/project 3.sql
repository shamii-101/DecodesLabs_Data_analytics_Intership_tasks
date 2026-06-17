SELECT * FROM project3.`dataset for data analytics`
limit 10;
SELECT *
FROM project3.`dataset for data analytics`
WHERE OrderStatus IN ('Delivered','Cancelled'); 
SELECT *
FROM project3.`dataset for data analytics`
WHERE OrderStatus ='Delivered'; 
select *
from project3.`dataset for data analytics`
order by TotalPrice DESC;
select *
from project3.`dataset for data analytics`
order by Date desc;
select Product, count(*)
from project3.`dataset for data analytics`
group by Product;
select count(*)
from project3.`dataset for data analytics`;
select sum(TotalPrice)
from project3.`dataset for data analytics`;
select avg(ItemInCart)
from project3.`dataset for data analytis`;

