SELECT
	f.fid
	, f.title
	, f.category
	, f.length
FROM film_list AS f
LIMIT 10 OFFSET 30