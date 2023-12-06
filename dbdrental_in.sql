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