'''
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

My name is Michele
Then I would see the string:

 # Michele is name My
shown back to me.
'''

def reverse_str(inp_str):
    result = inp_str.split()
    return result[::-1]

Long_string = "My name is Michele"
#Long_string = str(input('Enter your string: '))      User input
a = ' '.join(reverse_str(Long_string))

print('Initial Input String: ' +Long_string)
print('Reverse Order: '+a)