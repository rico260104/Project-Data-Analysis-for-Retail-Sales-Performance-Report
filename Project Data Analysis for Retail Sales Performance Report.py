select 
year (order_date) as years,
sum(sales) as sales,
count(distinct order_id) as number_of_order
from calendar import weekheader
from itertools import product
from select import select
from dqlab_sales_store
where order_status = 'Order Finished'
group by 1
order by 1

select year(order_date) as years,
product_sub_category,
sum(sales) as sales
from dqlab_sales_store y
where order_status = 'Order Finished'
and year(order_date) in (2011,2012) 
# membuat rentang 2011 2012 between 2011 and 2012
group by 1,2
order by 1,3 desc 
# desc untuk mengurutkan dari terbesar ke terkecil

select
years,
sales,
promotion_value,
ROUND((promotion_value/sales)*100,2) as burn_rate_percentage
#ROUND untuk membulatkan nilai ,2 (mengambil dua angka setelah koma)
from (select extract(YEAR FROM order_date) as years,
SUM(discount_value) as promotion_value, SUM(sales) as sales
from dqlab_sales_store
where order_status = 'Order Finished'
group by 1) a
# a untuk alias
order by 1

#cte
with a as(
SELECT
(EXTRACT(YEAR FROM order_date)) AS years,
product_category,
product_sub_category,
SUM(discount_value) AS promotion_value,
SUM(sales) AS sales
FROM dqlab_sales_store
WHERE order_status = 'Order Finished' and EXTRACT(YEAR FROM order_date) ='2012'
GROUP BY 1,2,3)
SELECT
years,
product_sub_category,
product_category,
sales,
promotion_value,
round((promotion_value/sales)*100,2) AS burn_rate_percentage
FROM a
ORDER BY 4 DESC

select year(orer_date) as years,
count(distinct customer) as number_of_customer
from dqlab_sales_store
where 
order_status = 'Order Finished'
group by 1
#group untuk menjadi 1 grup yang sama misa a,a,b grup a,b 
order by 1
#order untuk mengurutkan terkecil