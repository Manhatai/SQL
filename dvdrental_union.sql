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