# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) 
# and another number. The function decides whether or not the given number is inside the list and returns (then prints) 
# an appropriate boolean.

# find is a function that takes an ordered list of numbers and another number,
# returning true or false whether the element appears in the list

def elementsearch(list1, number):
    for element in list1:
        if element == number:
            return True
    return False

a = [1,5,7,9,11,15,18,20]
print(elementsearch(a,5))
print(elementsearch(a,8))
print(elementsearch(a,11))
print(elementsearch(a,14))
        