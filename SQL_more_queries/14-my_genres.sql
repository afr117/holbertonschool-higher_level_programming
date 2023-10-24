-- List all genres of the show Dexter from hbtn_0d_tvshows
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT DISTINCT tg.name
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE ts.title = 'Dexter'
ORDER BY tg.name;
