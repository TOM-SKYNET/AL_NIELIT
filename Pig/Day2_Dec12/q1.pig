
m = load  '/vimala/movies.txt' using PigStorage(',') as (slno:int, mname:chararray, year:int,rating:float);
