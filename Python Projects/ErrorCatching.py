'''
Given this solution to Exercise 9, modify it to have one level of user feedback: if the user does not enter a number between 1 and 9,
tell them. Don\’t count this guess against the user when counting the number of guesses they used.

'''

import random
number = random.randint(1,9)
numb_guess = 0

while True:
    while True:
        try:
            guess = int(input('Enter the number between 1 and 9: '))
            if guess>=1 and guess<=9:
                break
            else:
                print('You must enter the number between 1 and 9')
        except ValueError:
            print('You must enter a number')
            
    
    numb_guess +=1
    if guess == number:
        break

print(f"You guessed {number} right in {numb_guess} attempts")

