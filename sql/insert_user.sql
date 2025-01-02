insert into user(name, age, height, sex)
select 
    d.name,
    d.age,
    d.height,
    d.sex
from (
select 
    ? as name,
    ? as age,
    ? as height,
    ? as sex    
) d 
left join user u
    on UPPER(d.name) = UPPER(u.name)
where u.id is null
