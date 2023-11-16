-- genre
curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows;
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_shows_genres.genre_id;