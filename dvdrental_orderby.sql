SELECT
	country, city, name
FROM public.customer_list
ORDER BY country, city
LIMIT 10 OFFSET 110