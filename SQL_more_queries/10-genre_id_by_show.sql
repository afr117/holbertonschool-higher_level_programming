--  lists all shows contained in the database hbtn_0d_tvshows.
--  that have at least one genre linked
SELECT s.title as title, g.id as genre_id
FROM tv_shows s JOIN tv_show_genres g ON s.genre_id = g.id
ORDER BY s.title ASC, g.id ASC;
