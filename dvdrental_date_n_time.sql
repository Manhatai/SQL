--SELECT NOW()::TIME, CURRENT_TIMESTAMP, CURRENT_DATE, CURRENT_TIME
SELECT
	r.rental_date
	, r.return_date
	, (r.rental_date + INTERVAL '3 MONTHS')::DATE AS expected_return
	, AGE(r.return_date, r.rental_date) AS duration
	, DATE '2030-05-01'
FROM rental r