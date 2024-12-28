from sqliteutil import SqliteUtil

def initDatabase(util:SqliteUtil):
    util.executeSqlFromFile("create_user")
    util.executeSqlFromFile("create_meal")
    util.executeSqlFromFile("create_weight")
    util.executeSqlFromFile("create_meallog")
    # TODO: create meal log

def insertUser(util:SqliteUtil, name:list):
    t = [name]
    util.executeSqlFromFileWithParam('insert_user', t)

def insertMeal(util:SqliteUtil, username:str, m:str, cal:int, carb:int, f:int, p:int):
    t = [username, m, cal, carb, f, p]
    util.executeSqlFromFileWithParam('insert_meal', t)

# TODO
def insertWeight(util:SqliteUtil, userid:int, weight:int, measuredate:int):
    t = [userid, weight, measuredate]
    util.executeSqlFromFileWithParam('insert_weight', t)

# TODO
def insertMealLog():
    pass

def main():
    sql = SqliteUtil()
    initDatabase(sql)
    # insertUser(sql, 'Bob')
    # insertMeal(sql, 'Bob', 'Philly Cheesesteak', 604, 50, 40, 40)
    # print(sql.queryToList('''select * from user'''))
    # res = sql.queryToVal("""select id from user where name = 'Will'""", bool)
    # print(res , type(res))
    # print(sql.queryToDict("""select * from meal"""))
    insertWeight(sql, 1, 170, '12/27/2024')



if __name__ == "__main__":
    main()
