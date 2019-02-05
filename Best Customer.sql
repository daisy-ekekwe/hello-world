select customers.FirstName, customers.LastName, sum(invoices.Total) as MoneySpent
from invoices
inner join customers on invoices.CustomerId=customers.CustomerId;