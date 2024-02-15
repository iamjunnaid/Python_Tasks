#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random

randnum = random.randint(1,9)
guessnum = 0
count = 0
while guessnum != randnum and guessnum != "exit":
    guessnum = input("Enter a guess between 1 to 9: ")

    if guessnum == "exit":
        break

    guessnum = int(guessnum)
    count += 1

    if guessnum < randnum:
        print("Too low")
    elif guessnum > randnum:
        print("Too high")
    else:
        print("Right!")
        print("You took only", count, "tries!")
