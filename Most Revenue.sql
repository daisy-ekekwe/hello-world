SELECT BillingCountry, sum(total) as Revenue FROM invoices
group by BillingCountry
order by Revenue 
desc;
