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









"""