select distinct BillingCountry, sum(total) as invoice from invoices
order by Total;