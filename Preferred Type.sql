select m.name, count(t.mediatypeid) as 
from tracks t
inner join media_types m on t.mediatypeid = m.mediatypeid 
group by t.mediatypeid
order by amount
desc 
