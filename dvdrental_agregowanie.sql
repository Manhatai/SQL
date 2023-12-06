SELECT
	category
	, COUNT(*) AS record_number
	, SUM(length) AS total_lenght
	, AVG(length) AS avg_length
FROM public.film_list
WHERE (category LIKE 'A%' OR category LIKE 'C%')
GROUP BY category
HAVING AVG(length) > 110
ORDER BY category