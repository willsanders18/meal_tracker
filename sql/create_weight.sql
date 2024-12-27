create table if not exists weight(
    id integer primary key,
    userid integer, 
    weight integer,
    measuredate TEXT,
    foreign key(userid) REFERENCES user(id)
)