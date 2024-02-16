#Ask the user for a number and determine whether the number is prime or not. 
#(For those who have forgotten, a prime number is a number that has no divisors.). 

import sys
number = int(input('Enter your number: '))
prime = False
if number > 0:
    for x in range(2, number-1):
        if number%x !=0:
            continue
        elif number%x == 0:
            sys.exit('Number is not prime.')
    sys.exit('Number is prime.')
else:
    sys.exit('Enter number greater than 0')