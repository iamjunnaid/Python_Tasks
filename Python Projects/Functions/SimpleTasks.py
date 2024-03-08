'''
Task 1: Assign a different name to function and call it through the new name
Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
'''

def display_student(name, age):
    print(name, age)

display_student("Emma", 26)

show_student = display_student
show_student("Jess",30)

'''
Task 2: Generate a Python list of all the even numbers between 4 to 30
'''
print('The Even list between 4 and 30 is: ',list(range(4,30,2)))

'''
Task 3: Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
'''

x = [4, 6, 8, 24, 12, 2]
print('The maximum number is: ',max(x))