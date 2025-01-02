'''
Diet Tracker Program
ISE 314 Final Project
Dr. Sambaturu
William Sanders, Midas Leung, Adam Horowitz
'''

# Importing necessary packages
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import random

# Variables to connect to database
con = sqlite3.connect('meals.db')
cur = con.cursor()

# These lines are only executed once to initialize the tables into the sqlite database
# cur.execute("CREATE TABLE user(name, age, sex, weight, height)")
# cur.execute("CREATE TABLE meals(name, fat, carbs, protein, calories)")

# Class utilized for future BMI chart
class Person:
    def __init__(self, name, age, height, weight, gender):
        self.name = name
        self.age = age
        self.height = height  # inches
        self.weight = weight  # pounds
        self.gender = gender
    
    # Function gets BMI based on inputed data
    def BMI(self):
       
        if self.height > 0:  
            bmi = (self.weight*703)/(self.height**2)
            return round(bmi, 1)
        else:
            return None  # Handle invalid height case

# Create instances of the Person class
people = [
    Person("John", 25, 71, 154, "Male"),
    Person("Anna", 30, 63, 110, "Female"),
    Person("Mike", 35, 69, 187, "Male"),
    Person("Sara", 28, 65, 198, "Female")
]

# Creates lists to be used for BMI chart
names = [person.name for person in people]
bmi_values = [person.BMI() for person in people]

# Function to insert user info into sql database
def addUser(name, age, sex, weight, height):
    cur.execute('''insert into user (name, age, sex, weight, height) values(?, ?, ?, ?, ?)
                    ''',(name, age, sex, weight, height))
    con.commit()

# Contains the main logic of the diet tracker program    
def main():
    new = input('Would you like to create a new user? (y/n): ')

    if new.lower() == 'y':
        name1 = input('Enter your name: ')
        age1 = int(input('Enter your age: '))
        sex1 = input('Enter your sex: ')
        weight1 = int(input('Enter your weight in pounds: '))
        height1 = int(input("Enter your height in inches: "))

        addUser(name1, age1, sex1, weight1, height1)
    else:
        print('Understood!')

    # While loop to keep program running until the user quits
    while True:
        ask = input('What would you like to do?\n Add Meal (a)\n BMI (b)\n Data Analysis (d)\n Maintenance Calories (m)\n Random Meal Suggestion (r)\n Quit (q)\n') 

        # If-statements for each possible user input
        if ask == 'a':
            # Getting user input
            name = input("Enter meal name: ")
            fat = int(input("Enter grams of fat: "))
            carbs = int(input("Enter grams of carbs: "))
            protein = int(input("Enter grams of protein: "))
            calories = fat*9 + carbs*4 + protein*4

            # Putting user input into database
            cur.execute('''insert into meals (name, fat, carbs, protein, calories) values(?, ?, ?, ?, ?)
                        ''',(name, fat, carbs, protein, calories))
            con.commit()

            # Prints out the name of the specific meal added to the database
            res = cur.execute("SELECT name FROM meals")
            namelist = res.fetchall()
            for i in namelist:
                if str(i[0]) == name:
                    mealname = str(i[0])
                    break
            print(f'{mealname} has been added to the database')

        elif ask == 'b':
            # Gets user weight
            res1 = cur.execute("SELECT weight FROM user")
            weightlist = res1.fetchall()
            weight = weightlist[0][0]
            
            # Gets user height
            res2 = cur.execute("SELECT height FROM user")
            heightlist = res2.fetchall()
            height = heightlist[0][0]

            # Calculates user BMI and rounds it
            bmi = (weight*703)/(height**2)
            bmi = round(bmi, 1)

            # Checks to make sure user BMI isn't already in the list
            if bmi not in bmi_values:
                bmi_values.append(bmi)
                res3 = cur.execute("SELECT name FROM user")
                namelist1 = res3.fetchall()
                name1 = namelist1[0][0]
                names.append(name1)

            print(f'Your BMI is {round(bmi, 1)}')
            print('Here is a graph comparing your BMI to other user BMIs')

            # Matplotlib used to plot a chart comparing user BMI to other sample BMI's
            plt.figure(figsize=(8, 5))
            plt.bar(names, bmi_values, color='skyblue', edgecolor='black')


            plt.axhline(18.5, color='gray', linestyle='--', label='Underweight Threshold')
            plt.axhline(24.9, color='green', linestyle='--', label='Ideal Weight Threshold')
            plt.axhline(29.9, color='orange', linestyle='--', label='Overweight Threshold')


            plt.title("BMI for Individuals", fontsize=16)
            plt.xlabel("Individuals", fontsize=12)
            plt.ylabel("BMI Value", fontsize=12)
            plt.legend()


            plt.tight_layout()
            plt.show()

        elif ask == 'd':
            df = pd.read_sql_query("SELECT * FROM meals", con) # Collects every bit of meal info from table into a pandas dataframe
            print(df)

            # Calculated means of each column
            calMean = df['calories'].mean()
            fatMean = df['fat'].mean()
            carbsMean = df['carbs'].mean()
            proMean = df['protein'].mean()

            # Displays means to user
            print(f'Average calorie intake per meal: {round(calMean)}')
            print(f'Average fat (g) intake per meal: {round(fatMean)}')
            print(f'Average carb (g) intake per meal: {round(carbsMean)}')
            print(f'Average protein (g) intake per meal: {round(proMean)}')

        elif ask == 'm':
            # Calculates an estimated maitenance calorie intake for the user
            res = cur.execute("SELECT weight FROM user")
            weightlist = res.fetchall()
            weight = weightlist[0][0]
            print(f'Your estimated maintenance calories are {weight*15}')

        elif ask == 'r':

            # Dictionary of meals
            meals_dict = {
                'Grilled Chicken with Rice and Broccoli' : '\nCalories: 350\n Fat: 10g\n Carbs: 30g\n Protein: 30g',
                'Grilled Chicken Salad' : '\nCalories: 350\n Fat: 12g\n Carbs: 20g\n Protein: 35g',
                'Salmon with Quinoa and Steamed Broccoli' : '\nCalories: 450\n Fat: 18g\n Carbs: 30g\n Protein: 40g',
                'Tofu and Veggie Stir-fry' : '\nCalories: 400\n Fat: 10g\n Carbs: 60g\n Protein: 20g',
                'Beef Tacos' : '\nCalories: 500\n Fat: 20g\n Carbs: 45g\n Protein: 30g'
            }

            # Gets a random meal and displays it to the user
            meal, macros = random.choice(list(meals_dict.items()))
            print(f'Here is a random healthy meal suggestion: {meal} {macros}')

        # Breaks the loop thus ending the program
        elif ask == 'q':
            break
        else:
            print('Invalid input, please try again!')

    print('Thank you')

main()
con.close() # Always a good practice to close the connection to the databse once the program is done running
  
