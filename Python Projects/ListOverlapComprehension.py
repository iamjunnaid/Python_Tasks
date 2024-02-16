#Take two lists, say for example these two:

#	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
#Make sure your program works on two lists of different sizes. 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []

for x in set(a):
    if x in b:
        common.append(x)

print('The Overlapping common numbers from given lists are: ',common )

# Extra:Randomly generate two lists to test this

import random

c = random.sample(range(1,30),12)
d = random.sample(range(1,45),15)
extra_common = []
for z in set(c):
    if z in d:
        extra_common.append(z)

print('Random List 1: ',c)
print('Random List 2: ', d)
print('The Random common numbers are: ',extra_common)