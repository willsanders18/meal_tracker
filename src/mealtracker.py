from sqliteutil import SqliteUtil

class Tracker:
    def __init__(self, util:SqliteUtil):
        self.util = util
    
    def initDatabase(self):
        self.util.executeSqlFromFile("create_user")
        self.util.executeSqlFromFile("create_meal")
        self.util.executeSqlFromFile("create_weight")
        self.util.executeSqlFromFile("create_meallog")

    def insertUser(self, name:list):
        t = [name]
        self.util.executeSqlFromFileWithParam('insert_user', t)

    def insertMeal(self, username:str, m:str, cal:int, carb:int, f:int, p:int):
        t = [username, m, cal, carb, f, p]
        self.util.executeSqlFromFileWithParam('insert_meal', t)

    def insertWeight(self, username:str, weight:int, measuredate:int):
        t = [username, weight, measuredate]
        self.util.executeSqlFromFileWithParam('insert_weight', t)

    def insertMealLog(self, username:str, mealname:str, date:str):
        t = [username, mealname, date]
        self.util.executeSqlFromFileWithParam('insert_meallog', t)