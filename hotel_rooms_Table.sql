CREATE TABLE rooms
(
	room_id SERIAL PRIMARY KEY,
	room_number INTEGER NOT NULL,
	max_persons INTEGER NOT NULL,
	class INTEGER NOT NULL
);