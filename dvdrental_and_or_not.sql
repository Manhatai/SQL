SELECT
	*
FROM customer AS c
WHERE c. store_id = 1 AND NOT (c.first_name LIKE 'J%' OR c.last_name LIKE 'R%')