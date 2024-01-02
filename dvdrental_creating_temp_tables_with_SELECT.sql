--SELECT *  INTO my_actor FROM actor
--SELECT * FROM my_actor
--DROP TABLE my_actor
/*
SELECT 
	a.first_name, a.last_name, COUNT(*)
	INTO TEMPORARY temp_actor
FROM actor a
LEFT JOIN film_actor as fa ON fa.actor_id = a.actor_id
GROUP BY a.first_name, a.last_name
*/

-- SELECT * INTO TEMP temp_actor2 FROM actor WHERE 1 = 0
SELECT * FROM temp_actor2