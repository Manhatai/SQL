/*
SELECT 
	f.title
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON f.film_id = fa.film_id
WHERE a.first_name = 'Bette' AND a.last_name = 'Nicholson'
*/
SELECT f.title
FROM film f
WHERE f.film_id IN
	(SELECT
		fa.film_id
	FROM actor a
	JOIN film_actor fa ON fa.actor_id = a.actor_id
	WHERE a.first_name = 'Bette' AND a.last_name = 'Nicholson')