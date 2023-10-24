SELECT s.title as title, tv_genres.id as genre_id
FROM tv_shows s
JOIN tv_show_genres ON s.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY s.title ASC, tv_genres.id ASC;
