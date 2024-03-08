'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

word = str(input('Enter the word: '))
reverse = word[::-1]

print(word+' in backward is: ' +reverse)

if reverse == word:
    print('This word is palindrome: ' + word)
else:
    print('This word is not palindrome: ' + word)