insert into weight(userid, weight, measuredate) 
with input_data as (
    select 
    ? as username,
    ? as weight,
    ? as measuredate
),
data as (
    select
    u.id as userid,
    i.weight,
    i.measuredate
    from input_data i
    inner join user u
        on u.name = i.username
)
select 
d.userid,
d.weight,
d.measuredate
from data d
left join weight w
    on w.measuredate = d.measuredate
    and w.userid = d.userid
where w.id is null
