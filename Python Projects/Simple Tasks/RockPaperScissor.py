'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of 
congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''

import sys


user1 = input('Enter 1st username: ')
user2 = input('Enter 2nd username: ')

userans1 = input("%s, what do you choose - Rock/Paper/Scissor: " %user1)
userans2 = input("%s, what do you choose - Rock/Paper/Scissor: " %user2)

def compare(u1,u2):

    if u1 == u2:
        return('It is a tie')

    elif u1 == 'rock':
        if u2 == 'scissor':
            return('Rock wins')
        else:
            return('Paper Wins')
        
    elif u1 == 'scissor':
        if u2 == 'paper':
            return('Scissor Wins!')
        else:
            return('Rock Wins!')
        
    elif u1 == 'paper':
        if u2 == 'rock':
            return('Paper Wins!')
        else:
            return('Scissor Wins!')
        
    else:
        return('Invalid input')
        sys.exist()

print(compare(userans1,userans2))
        

 
    
