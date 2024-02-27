# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all 
# prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

def FileRead(filename):
    list_return = []
    with open(filename) as f:
        line = f.readline()
        while line:
            list_return.append(int(line))
            line = f.readline()
    return list_return

primelist = FileRead('Prime.txt')
Happylist = FileRead('HappyNumbers.txt')

OvelappingNumber = [elem for elem in primelist if elem in Happylist]

print('The Overlapping numbers are: ',OvelappingNumber)