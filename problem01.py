#PROBLEM STATEMENT:
#Write a program to repeat the string "GOOD MORNING" n times. Here n is an integer entered by the user.

str1 = "GOOD MORNING"
n = int(input("Enter the number of times you want to repeat 'GOOD MORNING':"))
repeated_string = str1 * n
print(repeated_string)