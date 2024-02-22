# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed 
# correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is 
# a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses 
# the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell 
# the user at the end.

import random

def gen_random():
    return ''.join(random.sample('0123456789',4))

def count_cows_bulls(secret_number, user_guess):
    cows = 0
    bulls = 0
    for i in range(len(secret_number)):
        if user_guess[i] == secret_number[i]:
            cows +=1
        elif user_guess[i] in secret_number:
            bulls +=1
    return cows, bulls


def main():
    print('Welcome to Cows and Bulls Game')
    secret_number = gen_random()
    num_guess = 0

    while True:
        user_guess = input('Enter the 4 digit number: ')
        if len(user_guess) !=4 or not user_guess.isdigit():
            print('Only Enter 4 digits')
            continue
        num_guess +=1
        cows, bulls = count_cows_bulls(secret_number, user_guess)
        print(f"{cows} cow, {bulls} bull")

        if cows == 4:
              print("Congratulations! You've guessed the correct number", {secret_number})
              print('Total Guess: ',num_guess)
              break
if __name__ == "__main__":
    main()