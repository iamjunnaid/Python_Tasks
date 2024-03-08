'''
Input two Random list and write a program that returns a list that contains only the elements that are 
common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
compare them with each other to see 
'''

import random
randlist11=[]
randlist22=[]
commonlist = []

numlist1 = int(input("How many integers in the list 1:"))
for i1 in range(1,numlist1+1):
        randlist11.append(random.randint(1,10))


numlist2 = int(input("How many integers in the list 2:"))
for i2 in range(1,numlist2+1):
        randlist22.append(random.randint(1,10))

print('List 1: ' ,randlist11)
print('List 2: ' ,randlist22)
        
# Comparison between Two Lists

for x in set(randlist11):
    if x in set(randlist22):
        commonlist.append(x)

print('The common integers in the both lists are: ' ,commonlist)