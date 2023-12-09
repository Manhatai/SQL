SELECT
	rental_date
	, customer_id
	, return_date
	, CASE
		WHEN return_date IS NULL THEN 'UNKNOWN'
		ELSE CAST(return_date AS CHAR(10))
	END AS description
	, COALESCE(CAST(return_date AS CHAR(10)), 'UNKNOWN') AS description_2
FROM rental
WHERE rental_date >= '2005-08-23 22:26:47'
ORDER BY rental_date