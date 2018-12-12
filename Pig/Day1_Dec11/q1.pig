movies = LOAD '/vimala/movies.txt' USING PigStorage(',') as (sl_no:int, moviename:chararray, year:int, rating:float); 
dump movies;

filter_data = FILTER movies BY year == 1994;
dump filter_data;

filter_rating = FILTER movies BY rating == 3.5;
dump filter_rating;

STORE filter_rating INTO '/vimala/s4/' USING PigStorage (',');

grouped =  Group movies All;

