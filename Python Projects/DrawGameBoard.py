'''
Time for some fake graphics! Let’s say we want to draw game boards that look like this:
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
'''

hor = '---'.join("    ")
ver = '   '.join("||||")
print('\n'.join((hor,ver,hor,ver,hor,ver,hor)))