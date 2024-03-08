'''
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself again and again.

'''

def recursiv(number):
    if number:
        return number + recursiv(number-1)
    else:
        return 0
    
print(f"The Recursive answer for Number 10 is :",recursiv(10))