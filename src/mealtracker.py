from sqliteutil import SqliteUtil

class Tracker:
    def __init__(self, util:SqliteUtil):
        self.util = util
        self.username = None
        self.userId = None
    
    def initDatabase(self):
        self.util.executeSqlFromFile("create_user")
        self.util.executeSqlFromFile("create_meal")
        self.util.executeSqlFromFile("create_weight")
        self.util.executeSqlFromFile("create_meallog")

    def setUsername(self, username:str):
        self.username = username
        self.userId = self.getUserId(username)

    def getUserId(self, username:str):
        q = self.util._getSqlFromFile('get_user_id')
        return self.util.queryToValWithParam(q, [username], int)


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
        self.setUsername(n)

    def newMeal(self):
        name = input("Enter meal name: ")
        fat = int(input("Enter grams of fat: "))
        carbs = int(input("Enter grams of carbs: "))
        protein = int(input("Enter grams of protein: "))
        calories = fat*9 + carbs*4 + protein*4

