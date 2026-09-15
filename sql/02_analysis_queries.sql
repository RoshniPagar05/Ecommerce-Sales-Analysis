USE ecommerce_db;

-- 1. Total Revenue
SELECT SUM(quantity * unit_price) AS total_revenue
FROM sales
WHERE order_status = 'Completed';


-- 2. Total Orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM sales;


-- 3. Total Customers
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM sales;


-- 4. Total Products
SELECT COUNT(DISTINCT product) AS total_products
FROM sales;


-- 5. Best Selling Products
SELECT
    product,
    SUM(quantity) AS units_sold
FROM sales
WHERE order_status = 'Completed'
GROUP BY product
ORDER BY units_sold DESC;


-- 6. Revenue by Category
SELECT
    category,
    SUM(quantity * unit_price) AS revenue
FROM sales
WHERE order_status = 'Completed'
GROUP BY category
ORDER BY revenue DESC;


-- 7. Revenue by State
SELECT
    state,
    SUM(quantity * unit_price) AS revenue
FROM sales
WHERE order_status = 'Completed'
GROUP BY state
ORDER BY revenue DESC;


-- 8. Monthly Revenue
SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(quantity * unit_price) AS revenue
FROM sales
WHERE order_status = 'Completed'
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;


-- 9. Top 10 Customers
SELECT
    customer_id,
    customer_name,
    SUM(quantity * unit_price) AS total_spent
FROM sales
WHERE order_status = 'Completed'
GROUP BY customer_id, customer_name
ORDER BY total_spent DESC
LIMIT 10;


-- 10. Payment Method Analysis
SELECT
    payment_method,
    COUNT(*) AS number_of_orders
FROM sales
GROUP BY payment_method
ORDER BY number_of_orders DESC;


-- 11. Average Order Value
SELECT AVG(order_total) AS average_order_value
FROM (
    SELECT
        order_id,
        SUM(quantity * unit_price) AS order_total
    FROM sales
    WHERE order_status = 'Completed'
    GROUP BY order_id
) AS orders;