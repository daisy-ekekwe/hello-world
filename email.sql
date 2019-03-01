SELECT c.FirstName, c.LastName, c.Email, g.name as Genre
From customers c
inner Join invoices i on c.customerID = i.customerID
inner join tracks t on t.GenreID = g.GenreID
inner join genres g on t.GenreID = g.GenreID
where g.genreid = 1
Group by c.email
