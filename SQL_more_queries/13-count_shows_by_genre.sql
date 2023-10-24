-- List all genres from hbtn_0d_tvshows and display the number of shows linked to each
-- Display each record as <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre, and the second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
SELECT tg.name AS genre, COUNT(tsg.show_id) AS number_of_shows
FROM tv_genres tg
LEFT JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
GROUP BY tg.id
HAVING COUNT(tsg.show_id) > 0
ORDER BY number_of_shows DESC;
