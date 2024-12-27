from sqliteutil import SqliteUtil

def initDatabase(util:SqliteUtil):
    util.executeSqlFromFile("create_user")
    util.executeSqlFromFile("create_meal")
    util.executeSqlFromFile("create_weight")

def main():
    sql = SqliteUtil()
    initDatabase(sql)



if __name__ == "__main__":
    main()
