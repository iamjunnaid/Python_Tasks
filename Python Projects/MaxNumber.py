'''
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the 
Python max() function!
'''

def max_number(a,b,c):
    maximum_num = 0
    if a>b and b>c:
        maximum_num = a
        print(maximum_num)
    elif a<b and b>c:
        max_number = b
        print(maximum_num)
    elif a<b and b<c:
        maximum_num = c
        print(maximum_num)
    elif a>b and b<c and a<c:
        maximum_num =c
        print(maximum_num)

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
max_number(num1,num2,num3)