# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase 
# letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user 
# asks for a new password. Include your run-time code in a main method.


import string
import random
passw = []

def pw_genera(size):
    charact = string.ascii_letters + string.digits + string.punctuation
    for x in range(size):
        passw.append(random.choice(charact))

    return ''.join(passw)

print(pw_genera(int(input('How many characters in your password?'))))