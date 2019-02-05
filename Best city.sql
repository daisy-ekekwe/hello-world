select distinct BillingCity, sum(total) as invoice from invoices
order by Total;