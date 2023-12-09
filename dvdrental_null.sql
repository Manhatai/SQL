--SELECT
--	COUNT(*)
--FROM rental
--WHERE return_date IS NULL
--ORDER BY return_date DESC

--CREATE TEMPORARY TABLE numbers
--(number INTEGER NULL)

--INSERT INTO numbers VALUES (10), (20), (30), (NULL)

--SELECT AVG(number) FROM numbers

--DROP TABLE numbers

SELECT
	COUNT(DISTINCT customer_id) AS count_of_customers
FROM rental

