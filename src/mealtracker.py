from sqliteutil import SqliteUtil

class Tracker:
    def __init__(self, util:SqliteUtil):
        self.util = util
    
    def initDatabase(self):
        self.util.executeSqlFromFile("create_user")
        self.util.executeSqlFromFile("create_meal")
        self.util.executeSqlFromFile("create_weight")
        self.util.executeSqlFromFile("create_meallog")

    def insertUser(self, name:str, a:int, h:int, s:str):
        t = [name, a, h, s]
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

    def getAllNames(self):
        q = self.util._getSqlFromFile('select_all_names')
        names = self.util.queryToList(q)

        namesList = []

        for i in names:
            namesList.append(i[0])
        return namesList

    def newUser(self):
        n = str(input('Enter your name: '))
        a = int(input('Enter your age: '))
        h = int(input('Enter your height in inches: '))
        s = str(input('Enter your sex: '))
        self.insertUser(n, a, h, s)