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



"""