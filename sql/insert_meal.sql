insert into meal (userid, mealname, calories, carbs, fat, protein)
with data as (
    select 
        u.id as userid,
        d.mealname,
        d.calories,
        d.carbs,
        d.fat,
        d.protein
    from (
        select
            ? as username,
            ? as mealname,
            ? as calories,
            ? as fat,
            ? as carbs,
            ? as protein
            ) d
    inner join user u
        on u.name = d.username
)
select 
    d.userid,
    d.mealname,
    d.calories,
    d.carbs,
    d.fat,
    d.protein
from data d
left join meal m 
    on m.mealname = d.mealname
    and m.userid = d.userid
where m.id is null