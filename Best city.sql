select BillingCity, sum(total) as invoice from invoices
group by BillingCity
order by invoice desc
limit 1;