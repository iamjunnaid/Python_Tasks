'''
Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.
remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.

'''

def charac_remove(words,n):
    print('Original string:', words)
    x = words[n:]
    return x

print("Removing characters from a string")
print(charac_remove("pynative", 4))
print(charac_remove("pynative", 2))


