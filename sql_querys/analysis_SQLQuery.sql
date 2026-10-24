use blinkit
select * from salarys

select sum(estimated_monthly_gross_inr) as total_earings from salarys

select count(city) as no_of_city from salarys

SELECT *FROM (SELECT city, SUM(delivery_earnings_inr) AS total_earnings
    FROM salarys GROUP BY city) AS result

select payment_frequency from salarys group by payment_frequency

select * from products

select product_name,count(product_name) as item_count,sum(price) as total_price
     from products group by product_name

select  product_name, count( product_name) as item_count,min(min_stock_level) as min_stock_level,
     max(max_stock_level) as max_stock_level from 
    (select * from products where mrp <300) as ps group by  product_name

select * from orders

select payment_method,count(payment_method) as no_of_orders_used from 
orders group by payment_method

select delivery_status,count(delivery_status) as delivery_status_count
from orders group by delivery_status

select * from order_items

select sum(order_id) as no_of_orders,sum(unit_price) as total_price from order_items

select * from marketing_performance

select target_audience,count(target_audience) as counts from marketing_performance
group by target_audience

select date,count(date) as spending_count,sum(spend) as spend,
sum(revenue_generated) as profit from marketing_performance group by date

select * from customers

select area,count(area) as no_of_users from customers group by area

select area,customer_segment,count(customer_segment) as status_count,
sum(total_orders) as total_orders,sum(avg_order_value) as avg_order_value
from customers group by area,customer_segment

select * from blinkit_investment_data

select count(company) as investers_count,sum(amount_usd_m) as amount_million,
sum(amount_inr_crore_approx) as amount_crores from blinkit_investment_data