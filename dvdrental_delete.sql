--SELECT * FROM actor ORDER BY actor_id DESC
--SELECT * FROM actor WHERE actor_id = 208

--DELETE FROM actor WHERE actor_id=208

/*
SELECT * FROM actor WHERE actor_id IN
	(SELECT
		a.actor_id
	FROM actor AS a
	LEFT JOIN film_actor AS fa ON fa.actor_id = a.actor_id
	WHERE fa.film_id IS NULL
	ORDER BY fa.film_id)
*/

DELETE FROM actor WHERE actor_id IN
	(SELECT
		a.actor_id
	FROM actor AS a
	LEFT JOIN film_actor AS fa ON fa.actor_id = a.actor_id
	WHERE fa.film_id IS NULL
	ORDER BY fa.film_id)
