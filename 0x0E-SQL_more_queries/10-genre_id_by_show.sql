-- genre
curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows;
SELECT tv_shows.title, tv_shows_genre.genre_id FROM tv_shows JOIN tv_shows_genre ON tv_shows.id = tv_shows_genre.id;