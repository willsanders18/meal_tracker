insert into user(name)
select 
    d.name
from (select ? as name) d 
left join user u
    on d.name = u.name
where u.id is null
