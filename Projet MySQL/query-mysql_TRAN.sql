/* --------------------
   Case Study Questions
   --------------------*/

-- 1. What is the total amount each customer spent at the restaurant?
-- 2. How many days has each customer visited the restaurant?
-- 3. What was the first item from the menu purchased by each customer?
-- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?
-- 5. Which item was the most popular for each customer?
-- 6. Which item was purchased first by the customer after they became a member?


-- 1. What is the total amount each customer spent at the restaurant?
SELECT 
    sales.customer_id,
    SUM(menu.price) AS total_spent
FROM `huy-nam_tran`.sales
JOIN `huy-nam_tran`.menu
	ON sales.product_id = menu.product_id
GROUP BY customer_id
ORDER BY customer_id;
--Result:
+──────────────+──────────────+
| customer_id  | total_spent  |
+──────────────+──────────────+
| A            | 76           |
| B            | 74           |
| C            | 36           |
+──────────────+──────────────+

-- 2. How many days has each customer visited the restaurant?

SELECT
    customer_id,
    COUNT (DISTINCT order_date) AS visited_days
FROM `huy-nam_tran`.sales
GROUP BY customer_id;

--Result:
+──────────────+───────────────+
| customer_id  | visited_days  |
+──────────────+───────────────+
| A            | 4             |
| B            | 6             |
| C            | 2             |
+──────────────+───────────────+

-- 3. What was the first item from the menu purchased by each customer?

WITH cte_order AS (
    SELECT
        sales.customer_id,
        menu.product_name,
        ROW_NUMBER() OVER(
            PARTITION BY sales.customer_id
            ORDER BY 
                sales.order_date,  
                sales.product_id
        ) AS item_order
        FROM `huy-nam_tran`.sales
        JOIN `huy-nam_tran`.menu
        ON sales.product_id = menu.product_id
)
SELECT * FROM cte_order
WHERE item_order = 1;
--Result:
+──────────────+───────────────+─────────────+
| customer_id  | product_name  | item_order  |
+──────────────+───────────────+─────────────+
| A            | sushi         | 1           |
| B            | curry         | 1           |
| C            | ramen         | 1           |
+──────────────+───────────────+─────────────+

-- 4. What is the 3 most purchased item on the menu and how many times was it purchased by all customers?
SELECT
    sales.product_id,
    menu.product_name,
    COUNT(sales.product_id) AS order_count
FROM `huy-nam_tran`.sales
INNER JOIN `huy-nam_tran`.menu
    ON sales.product_id = menu.product_id
GROUP BY
    menu.product_name
ORDER BY order_count DESC
LIMIT 1;
--Result:
+─────────────+───────────────+──────────────+
| product_id  | product_name  | order_count  |
+─────────────+───────────────+──────────────+
| 3           | ramen         | 8            |
+─────────────+───────────────+──────────────+

-- 5. Which item was the most popular for each customer?
SELECT
        sales.customer_id,
        menu.product_name,
        COUNT(*) as order_count
    FROM `huy-nam_tran`.sales
    JOIN `huy-nam_tran`.menu
        ON sales.product_id = menu.product_id
    GROUP BY 
        customer_id,
        product_name
    ORDER BY
        customer_id,
        order_count DESC;

SELECT customer_id,  product_name, order_count, rank_count
FROM (SELECT customer_id, product_id, count(product_id) AS order_count, 
        RANK() OVER(PARTITION BY  customer_id ORDER BY count(product_id) DESC) AS 'rank_count'
	FROM sales
	GROUP BY customer_id,product_id
	ORDER BY customer_id) as inner_table
JOIN menu USING(product_id)
where rank_count=1
ORDER BY customer_id ASC;

--Result:
+──────────────+───────────────+──────────────+─────────────+
| customer_id  | product_name  | order_count  | rank_count  |
+──────────────+───────────────+──────────────+─────────────+
| A            | ramen         | 3            | 1           |
| B            | ramen         | 2            | 1           |
| B            | curry         | 2            | 1           |
| B            | sushi         | 2            | 1           |
| C            | ramen         | 3            | 1           |
+──────────────+───────────────+──────────────+─────────────+

-- 6. Which item was purchased first by the customer after they became a member?
WITH after_member AS(
    SELECT customer_id, product_name, order_date, rank() 
        OVER(PARTITION BY customer_id ORDER BY order_date) AS first_order
    FROM sales JOIN menu USING(product_id)
    JOIN members USING(customer_id)
    WHERE order_date>=join_date
)

SELECT * FROM after_member
WHERE first_order=1;
--Result:
+──────────────+───────────────+─────────────+─────────────+
| customer_id  | product_name  | order_date  | first_order |
+──────────────+───────────────+──────────────+────────────+
| A            | curry         | 2021-01-07  | 1           |
| B            | sushi         | 2021-01-11  | 1           |
+──────────────+───────────────+─────────────+─────────────+

-- 7. Which item was purchased just before the customer became a member?
WITH before_member AS(
    SELECT customer_id, product_name, order_date, rank() 
        OVER(PARTITION BY customer_id ORDER BY order_date DESC) as first_order
    FROM sales JOIN menu USING(product_id)
    JOIN members USING(customer_id)
    WHERE order_date>=join_date
)

SELECT * FROM before_member
where first_order=1;
--Result:
+──────────────+───────────────+─────────────+──────────────+
| customer_id  | product_name  | order_date  | first_order  |
+──────────────+───────────────+─────────────+──────────────+
| A            | sushi         | 2021-01-01  | 1            |
| A            | curry         | 2021-01-01  | 1            |
| B            | sushi         | 2021-01-04  | 1            |
+──────────────+───────────────+─────────────+──────────────+

-- 8. What is the total items and amount spent for each member before they became a member?
WITH before_member AS(
    SELECT customer_id, product_id, order_date, join_date
	FROM sales JOIN members USING (customer_id)
	WHERE order_date < join_date
)

SELECT customer_id, COUNT(*) AS total_items, SUM(price) AS total_spent
FROM before_member
JOIN menu using(product_id)
GROUP BY customer_id
ORDER BY customer_id ASC;
--Result:
+──────────────+──────────────+──────────────+
| customer_id  | total_items  | total_spent  |
+──────────────+──────────────+──────────────+
| A            | 2            | 25           |
| B            | 3            | 40           |
+──────────────+──────────────+──────────────+

-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
SELECT customer_id, sum(
	CASE
		WHEN product_name='sushi' 
            THEN 2*price*10
            ELSE price*10
        END
        ) AS total_points
FROM sales 
JOIN menu USING(product_id)
GROUP BY customer_id;

--Result:
+──────────────+───────────────+
| customer_id  | total_points  |
+──────────────+───────────────+
| A            | 860           |
| B            | 940           |
| C            | 360           |
+──────────────+───────────────+




