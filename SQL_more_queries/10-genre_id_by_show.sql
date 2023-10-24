-- List all shows contained in the database hbtn_0d_tvshows that have at least one genre linked.
-- Display each record as tv_shows.title - tv_show_genres.genre_id
-- Sort results in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
