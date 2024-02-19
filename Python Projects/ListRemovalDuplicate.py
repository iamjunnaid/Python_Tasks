#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all
# the duplicates.

#Extras:

#Write two different functions to do this - one using a loop and constructing a list, and another using sets.

def dupli_loop(in_list1):
    end_list = []
    for x in in_list1:
        if x not in end_list:
            end_list.append(x)
    return end_list

def dupli_set(in_list2):
    return set(in_list2)

import random

a = [1,1,2,3,4,5,5,5,5,6,7,8]

print('Input List: ', a)
print('Output list from Loop: ', dupli_loop(a))
print('Output list from Set: ', dupli_set(a))


