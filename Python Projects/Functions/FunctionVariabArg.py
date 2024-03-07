'''
Write a program to create function func1() to accept a variable length of arguments and print their value.

Note: Create a function in such a way that we can pass any number of arguments to this function, and the function should process 
them and display each argument\'s value.
'''
import random
def func1(*args):
    for i in args:
        print(i)

func1(random.sample(range(0,50),10))