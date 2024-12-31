create table if not exists meallog(
    id integer primary key,
    userid integer, 
    mealid integer,
    date text,
    foreign key(userid) REFERENCES user(id)
    foreign key(mealid) REFERENCES meal(id)
)