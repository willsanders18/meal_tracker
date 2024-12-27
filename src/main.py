from sqliteutil import SqliteUtil

def initDatabase(util:SqliteUtil):
    util.executeSqlFromFile("create_user")
    util.executeSqlFromFile("create_meal")
    util.executeSqlFromFile("create_weight")

def insertUser(util:SqliteUtil, name:list):
    t = [name]
    util.executeSqlFromFileWithParam('insert_user', t)

def insertMeal():
    pass

def insertWeight():
    pass

def main():
    sql = SqliteUtil()
    initDatabase(sql)
    insertUser(sql, 'Will')



if __name__ == "__main__":
    main()
