#PROBLEM STATEMENT 03
#Program to calculate the year the user will turn 100 years old
import datetime
name = input("Enter your name:")
age = int(input("Enter your age:"))

current_year = datetime.datetime.now().year
year_turning_100 = current_year + (100 - age)
print("You will be turning 100 years in:", year_turning_100)