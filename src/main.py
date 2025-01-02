from sqliteutil import SqliteUtil
from mealtracker import Tracker


def main():
    sql = SqliteUtil()
    track = Tracker(sql)
    track.initDatabase()
    while True:
        username = str(input('Enter your name: '))
        # if username.capitalize()
        names = track.getAllNames()
        
        if username.capitalize() in names:
            print(f'{username} recognized')
            track.setUsername(username)
        else:
            ask = str(input(f'{username} not recognized, would you like to create a new user? (y/n): '))
            if ask.lower() == 'y':
                track.newUser()
            elif ask.lower == 'n':
                print('Thank you, quitting program...')
                break
            else:
                print('Invalid response, ending test...')
                break
        break

    while True:
        ask = input('What would you like to do?\n Add Meal (a)\n Quit (q)\n')

        if ask.lower() == 'a':
            track.newMeal()
        elif ask.lower() == 'q':
            break
        else:
            print('Invalid input, please try again')
            input('Press enter to continue...')
if __name__ == "__main__":
    main()
