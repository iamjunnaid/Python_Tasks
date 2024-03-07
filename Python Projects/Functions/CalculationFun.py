'''
Return multiple values from a function
Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. 
Also, it must return both addition and subtraction in a single return call.
'''

def calculation(a,b):
    addi = a+b
    subtra = a-b
    return addi, subtra

print(calculation(40,10))