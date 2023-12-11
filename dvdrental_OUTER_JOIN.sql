SELECT
	f.title, f.release_year
	, c.city AS store
FROM film AS f
LEFT JOIN inventory AS i ON i.film_id = f.film_id
LEFT JOIN store AS s ON s.store_id = i.store_id
LEFT JOIN address AS a ON a.address_id = s.address_id
LEFT JOIN city AS c ON c.city_id = a.city_id

WHERE f.title LIKE 'A%' --AND i.inventory_id IS NULL