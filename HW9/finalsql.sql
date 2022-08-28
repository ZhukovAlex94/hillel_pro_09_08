SELECT albums.Title AS 'Album name',
	   genres.Name AS Genre,
	   tracks.Composer AS 'Artist or Group',
	   SUM(tracks.Milliseconds)/60000 AS 'Duration(Minutes)',
	   SUM(tracks.Bytes)/1048576  AS 'Size (Mb)',
	   SUM(tracks.UnitPrice) AS 'Album price $',
	   COUNT(tracks.Name) AS 'Count tracks'
FROM tracks
	INNER JOIN albums ON tracks.AlbumId  = albums.AlbumId
	INNER JOIN genres ON tracks.GenreId  = genres.GenreId
	INNER JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
WHERE media_types.Name  = 'MPEG audio file'
GROUP BY albums.Title
ORDER BY genres.Name, tracks.Composer;



