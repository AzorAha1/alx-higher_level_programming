-- genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres LEFT JOIN tv_shows 
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id = NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC; 
