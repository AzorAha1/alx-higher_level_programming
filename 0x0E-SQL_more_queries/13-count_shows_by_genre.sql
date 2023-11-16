-- genre
SELECT tv_show_genres AS genre, COUNT(tv_shows) AS number_of_shows
FROM tv_show_genres
JOIN tv_shows ON tv_shows.id = tv_show_genres.genre_id