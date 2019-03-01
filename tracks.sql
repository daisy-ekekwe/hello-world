select ar.Name as Artist, count(t.trackID) as "Total Tracks"
from tracks t
inner join albums al on t.AlbumID = al.albumID
inner join artists ar ON al.artistID = ar.artistID
inner join genres g ON g.genreid = t.genreid
group by ar.artistID
order by "Total Tracks" DESC limit 10
