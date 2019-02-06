select customers.FirstName, customers.LastName, invoices.Total as "Money Spent"
from invoices
inner join customers on invoices.CustomerId = customers.CustomerId
group by customers.FirstName
order by "Money Spent" desc
limit 1;