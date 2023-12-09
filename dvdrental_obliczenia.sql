SELECT
	title
	, price
	, length AS length_in_mins
	, round(length / 60.0, 2) AS in_hours
	, round(price / (length / 60.0), 2) AS price_per_hour
FROM film_list
WHERE round(price / (length / 60.0), 2) >= 6
ORDER BY price_per_hour