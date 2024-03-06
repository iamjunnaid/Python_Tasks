'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?
'''

num = int(input('Enter a number'))
#mod = num%4
if num%4 == 0:
    print("Number is mulitple of 4")
elif num%2 == 0:
    print('Number is multiple of 2')
else:
    print(num,'Number is not a multiple of 2 or 4 ')