from sqliteutil import SqliteUtil
from mealtracker import Tracker

def newUser(tr:Tracker):
    n = str(input('Enter your name: '))
    a = int(input('Enter your age: '))
    h = int(input('Enter your height in inches: '))
    s = str(input('Enter your sex: '))
    tr.insertUser(n, a, h, s)

def main():
    sql = SqliteUtil()
    track = Tracker(sql)
    track.initDatabase()
    while True:
        username = str(input('Enter your name: '))
        # if username.capitalize()
        names = track.util.queryToList(track.util._getSqlFromFile('select_all_names'))
        namesList = []

        for i in names:
            namesList.append(i[0])
        
        if username.capitalize() in namesList:
            print(f'{username} recognized')
        else:
            ask = str(input(f'{username} not recognized, would you like to create a new user? (y/n): '))
            if ask.lower() == 'y':
                newUser(track)
            elif ask.lower == 'n':
                print('Thank you, quitting program...')
                break
            else:
                print('Invalid response, ending test...')
                break
        break

if __name__ == "__main__":
    main()
