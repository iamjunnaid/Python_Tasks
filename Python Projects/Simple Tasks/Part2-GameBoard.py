'''
As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.
'''


#import numpy
game = [[2,2,1],
[1,1,2],
[1,2,1]]

set_row = ()
set_col = ()

def line_match(game):
    for i in range(3):
        set_row = set(game[i])
        if len(set_row) == 1 and game[i][0] !=0:
            return game[i][0]
        return 0

#def column()
        
def diagonal_match(game):
    if game[1][1] !=0:
        if game[1][1] == game[0][0] == game[2][2]:
            return game[1][1]
        elif game[1][1] == game [0][2] == game[2][0]:
            return game[1][1]
    return 0

if line_match(game) > 0:
    print(str(line_match(game)) + str(" row wins"))
if diagonal_match(game) > 0:
    print(str(diagonal_match(game)) + str(" diagonal wins"))
        
    