-- selects shows with atleast one linked genre
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` as s
INNER JOIN `tv_show_genres` as g
ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;
