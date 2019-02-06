select BillingCountry, count(total) as invoice from invoices
group by BillingCountry
order by invoice desc;