'''
Given 2 non-negative integers, generate the next 10 numbers of a Fibonacci sequence seeded by those 2 numbers.
'''

def fibon(a, b, numbers = 10):
    sequence = [a,b]
    for x in range(numbers-2):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

a = 0
b = 1
fibonacci_series = fibon(a,b)
print('Next 10 numbers of Fibonacci Series are: ',fibonacci_series)
