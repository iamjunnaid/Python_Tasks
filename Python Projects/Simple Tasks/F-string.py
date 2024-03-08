'''
Implement the same exercise as Exercise 1 (Create a program that asks the user to enter their name and their age. Print out a 
message addressed to them that tells them the year that they will turn 100 years old), except use f-strings instead of the + operator 
to print the resulting output message.
'''

name = input('What is your name: ')
Born = int(input('When did you born: '))
age = 2024 - Born + 100
print(f"{name}, you'll be 100 years old at {age}")