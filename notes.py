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

"""