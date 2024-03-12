'''
Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

'''

def palind_num(number):
    print('Original Number: ',number)
    original_num = number
    reverse_number=0
    
    while number>0:
        reminder = number%10
        reverse_number = (reverse_number*10)+reminder
        number = number//10
        

    if original_num == reverse_number:
        print(f"Number is Palindrome: {original_num}")
        
    else:
        print(f"Number is not Palindrome:{original_num}")

palind_num(121)
palind_num(54)