from sqliteutil import SqliteUtil
from mealtracker import Tracker


def main():
    sql = SqliteUtil()
    track = Tracker(sql)
    track.initDatabase()
    # initDatabase(sql)
    # track.insertUser('Will', 21, 73, 'male')
    # # insertMeal(sql, 'Bob', 'Philly Cheesesteak', 604, 50, 40, 40)
    # # print(sql.queryToList('''select * from user'''))
    # # res = sql.queryToVal("""select id from user where name = 'Will'""", bool)
    # # print(res , type(res))
    # # print(sql.queryToDict("""select * from meal"""))
    # # insertMealLog(sql, 'Will', 'Philly Cheesesteak', '2024-12-28 00:09:00')
    # insertWeight(sql, 'Will', 185, '2024-12-28 00:28:00')
    while True:
        print('Test')
        break

if __name__ == "__main__":
    main()
