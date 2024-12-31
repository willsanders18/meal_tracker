insert into meallog(userid, mealid, date)
with data as ( 
select 
    u.id as userid,
    m.id as mealid,
    d.date
from (
select 
    ? as username,
    ? as mealname,
    ? as date
) d
inner join user u
        on u.name = d.username
inner join meal m
    on m.mealname = d.mealname
    and m.userid = u.id
)
select
    d.userid,
    d.mealid,
    d.date
from data d 
left join meallog l
    on d.date = l.date
    and d.userid = l.userid
    and d.mealid = l.mealid
where l.id is null