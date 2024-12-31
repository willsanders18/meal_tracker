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
def insertWeight(util:SqliteUtil, username:str, weight:int, measuredate:int):
    t = [username, weight, measuredate]
    util.executeSqlFromFileWithParam('insert_weight', t)

# TODO
def insertMealLog(util:SqliteUtil, username:str, mealname:str, date:str):
    t = [username, mealname, date]
    util.executeSqlFromFileWithParam('insert_meallog', t)

def main():
    sql = SqliteUtil()
    initDatabase(sql)
    # insertUser(sql, 'Bob')
    # insertMeal(sql, 'Bob', 'Philly Cheesesteak', 604, 50, 40, 40)
    # print(sql.queryToList('''select * from user'''))
    # res = sql.queryToVal("""select id from user where name = 'Will'""", bool)
    # print(res , type(res))
    # print(sql.queryToDict("""select * from meal"""))
    # insertMealLog(sql, 'Will', 'Philly Cheesesteak', '2024-12-28 00:09:00')
    insertWeight(sql, 'Will', 185, '2024-12-28 00:28:00')


if __name__ == "__main__":
    main()
