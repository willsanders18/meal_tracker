create table if not exists meal(
    id integer primary key,
    userid integer, 
    mealname text,
    calories integer,
    carbs integer,
    fat integer,
    protein integer,
    foreign key(userid) REFERENCES user(id)
)