CREATE VIEW customer_address
AS
SELECT
	c.first_name AS firstname, c.last_name as lastname, a.address, a.address2, ct.city, cn.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ct ON a.city_id = ct.city_id
JOIN country cn ON ct.country_id = cn.country_id
	