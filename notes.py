"""
Dzień 1:
Lekcja 1 i 2:

Nauczyłem się tworzyć bazy danych komendami, w tym tworzenie tabeli, wstawiania rekordów do tabeli i odtwarzania
baz danych.

Ważne komendy:
- CREATE DATABASE <nazwa>;

- (przykładowe tworzenie nowej tabeli:)
CREATE TABLE rooms
(
	room_id SERIAL PRIMARY KEY,
	room_number INTEGER NOT NULL,
	max_persons INTEGER NOT NULL,
	class INTEGER NOT NULL
);

- (przykładowe szukanie informacji w tabeli):
SELECT * FROM listprice
SELECT name, is_active, price FROM listprice

- (przykładowe dodawanie wpisów do tabeli:)
INSERT INTO listprice(name, is_active, price)
VALUES('hostel-room', False, 50);








Dzień 2:
Lekcja 3:

Ogólne wybieranie rekordów, czyli wprowadzenie do SELECT, WHERE, LIKE, AND OR NOT, DISTINCT, LIMIT i OFFSET, ORDER BY

Ważne komendy:
- (przykładowe zapytanie do bazy danych SELECT):
SELECT
	c.first_name AS "FIRST NAME"
	, c.last_name AS "LAST NAME"   -- AS jest opcjonalne
	, c.email AS "E-MAIL"
FROM customer AS c


- (przykładowe zapytanie do bazy danych WHERE):
SELECT
	*
FROM customer AS c
WHERE c.create_date >= '2006-02-14'


- (przykładowe zapytanie do bazy danych LIKE):
SELECT
	*
FROM customer AS c
WHERE c.last_name LIKE '%x%'

- (przykładowe zapytanie do bazy danych AND OR NOT):
SELECT
	*
FROM customer AS c
WHERE c. store_id = 1 AND NOT (c.first_name LIKE 'J%' OR c.last_name LIKE 'R%')


- (przykładowe zapytanie do bazy danych DISTINCT)
SELECT DISTINCT category, price FROM film_list

- (przykładowe zapytanie do bazy danych LIMIT i OFFSET)
SELECT
	f.fid
	, f.title
	, f.category
	, f.length
FROM film_list AS f
LIMIT 10 OFFSET 30

- (przykładowe zapytanie do bazy danych ORDER BY)





Dzień 3:
Lekcja 4:

Agregacje i inne usprawnienia

Ważne komendy:
- (agregowanie wartości:)
SELECT
	COUNT(*) AS record_number
	, MIN(price) AS min_price
	, MAX(price) AS max_price
	, SUM(length) AS total_length
	, AVG(length) AS avg_lenght
	, STRING_AGG(title, '; ') AS all_titles
FROM public.film_list

- (klauzula GROUP BY:)
SELECT
	category
	, price
	, COUNT(*) AS record_number
--	, MIN(price) AS min_price
--	, MAX(price) AS max_price
	, SUM(length) AS total_length
	, AVG(length) AS avg_lenght
FROM public.film_list
GROUP BY category, price
ORDER BY category, price
LIMIT 10 OFFSET 40

- (klauzula HAVING:)
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

- (klauzula BETWEEN:)
SELECT
	*
FROM public.film_list
WHERE length BETWEEN 100 AND 110
ORDER BY LENGTH

- (operator IN:)
SELECT
	*
FROM public.film_list
WHERE rating NOT IN ('G','PG','PG-13')

/*
"PG-13"
"PG"
"NC-17"
"R"
"G"
*/




Dzień 4:
Lekcja 5:

Typy, funkcje i NULL

Ważne komendy:
- (korzystanie z funkcji obliczeń:)
SELECT
	title
	, price
	, length AS length_in_mins
	, round(length / 60.0, 2) AS in_hours
	, round(price / (length / 60.0), 2) AS price_per_hour
FROM film_list
WHERE round(price / (length / 60.0), 2) >= 6
ORDER BY price_per_hour


- (NULL:)
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


- (COALESCE:)
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

- (funkcje testowe:)
SELECT
	UPPER(title) AS film_title
	, description
	, category
	, length
	, REPEAT('*', length / 10) AS duration
	, CONCAT(TRIM(title), ' (', category, ')') AS title_with_category
	, UPPER(SUBSTRING(category FROM 1 FOR 2))
	, RIGHT(UPPER(category), 2)
	, REVERSE(RIGHT(UPPER(category), 2))
	, LENGTH(description)
	, POSITION('amazing' IN LOWER(description))
FROM film_list
where POSITION('amazing' IN LOWER(description)) > 0

- (funkcje daty i czasu:)
--SELECT NOW()::TIME, CURRENT_TIMESTAMP, CURRENT_DATE, CURRENT_TIME
SELECT
	r.rental_date
	, r.return_date
	, (r.rental_date + INTERVAL '3 MONTHS')::DATE AS expected_return
	, AGE(r.return_date, r.rental_date) AS duration
	, DATE '2030-05-01'
FROM rental r

- (przegląd typów danych:)






Dzień 5:
Lekcja 6:

Pisanie zapytań do wielu tabel


- (relacje w relacyjnej bazie danych:)
--SELECT * FROM customer
--SELECT * FROM address WHERE address_id = 5
--SELECT * FROM city WHERE city_id = 463
SELECT * FROM country WHERE country_id = 50

- (złączenie tabel przez INNER JOIN)
SELECT
	c.first_name, c.last_name,
	a.address, a.district,
	ci.city, co.country
FROM customer AS c
INNER JOIN address AS a ON a.address_id = c.address_id
INNER JOIN city AS ci ON ci.city_id = a.city_id
INNER JOIN country AS co ON co.country_id = ci.country_id
--WHERE c.first_name = 'Mary' AND c.last_name = 'Smith'

- (OUTER JOIN:)
SELECT
	f.title, f.release_year
	, c.city AS store
FROM film AS f
LEFT JOIN inventory AS i ON i.film_id = f.film_id
LEFT JOIN store AS s ON s.store_id = i.store_id
LEFT JOIN address AS a ON a.address_id = s.address_id
LEFT JOIN city AS c ON c.city_id = a.city_id
WHERE f.title LIKE 'A%' --AND i.inventory_id IS NULL


- (podzapytania skalarne:)
SELECT
	f.title
	, f.rental_rate
	, (SELECT AVG(rental_rate) FROM film) AS avg_price
	, f.rental_rate - (SELECT AVG(rental_rate) FROM film) AS difference
FROM film AS f
WHERE f.rental_rate > (SELECT AVG(rental_rate) FROM film)

- (podzapytanie A JOIN:)



- (podzapytania skorelowane:)
SELECT
	f.title, f.rental_rate, f.length
FROM film AS f
WHERE f.length > (SELECT AVG(fsub.length) FROM film AS fsub WHERE fsub.rental_rate = f.rental_rate)
ORDER BY f.rental_rate, f.length

- (łączenie zapytań wyników przez UNION:)
SELECT
	c.first_name, c.last_name, a.address, a.address2, ct.city, cn.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ct ON a.city_id = ct.city_id
JOIN country cn ON ct.country_id = cn.country_id
UNION ALL
SELECT
	c.first_name, c.last_name, a.address, a.address2, ct.city, cn.country
FROM staff c
JOIN address a ON c.address_id = a.address_id
JOIN city ct ON a.city_id = ct.city_id
JOIN country cn ON ct.country_id = cn.country_id
UNION ALL
SELECT
	CAST(c.store_id AS VARCHAR(10)), NULL, a.address, a.address2, ct.city, cn.country
FROM store c
JOIN address a ON c.address_id = a.address_id
JOIN city ct ON a.city_id = ct.city_id
JOIN country cn ON ct.country_id = cn.country_id;



- (wprowadzenie do CREATE VIEW:)




Dzień 6:
Lekcja 7:

Modyfikacja danych


- (dodawanie rekordów - INSERT:)
SELECT * FROM actor ORDER BY actor_id DESC

--INSERT INTO actor
--VALUES (201, 'Brad', 'Pitt', now())


--INSERT INTO actor(first_name, last_name)
--VALUES ('Amy', 'Adams')

--INSERT INTO actor(first_name, last_name)
--VALUES ('Harrison', 'Ford'), ('Angelina', 'Jolie')
--RETURNING actor_id


- (UPDATE:)
SELECT * FROM actor WHERE actor_id = 208

/*
UPDATE actor
	SET
		first_name = 'Jolie',
		last_name = 'Angelina'
WHERE actor_id = 208
*/

/*
SELECT *
FROM actor
WHERE actor_id IN
	(SELECT
		fa.actor_id
	FROM film AS f
	JOIN film_actor AS fa ON fa.film_id = f.film_id
	WHERE f.film_id = 1)
*/

/*
UPDATE actor
	SET
		first_name = UPPER(first_name),
		last_name = UPPER(last_name)
WHERE actor_id IN
	(SELECT
		fa.actor_id
	FROM film AS f
	JOIN film_actor AS fa ON fa.film_id = f.film_id
	WHERE f.film_id = 1)
*/


SELECT * FROM actor



- (DELETE:)
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

- (tworzenie tabel tymczasowych poleceniem SELECT)
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

--SELECT * FROM temp_actor

-- SELECT * INTO TEMP temp_actor2 FROM actor WHERE 1 = 0
SELECT * FROM temp_actor2


- (przepisywanie rekordów za pomocą INSERT INTO ... SELECT:)
--SELECT * INTO TEMP temp_fa FROM film_actor;
--SELECT * FROM temp_fa
--INSERT INTO temp_fa
--VALUES
--	(1,1,NOW()),
--	(2,2,NOW()),
--	(3,3,NOW())

INSERT INTO temp_fa
SELECT * FROM film_actor;

SELECT COUNT(*) FROM temp_fa;



"""