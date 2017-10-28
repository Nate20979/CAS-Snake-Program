from random import randint

randNum = randint(0, 9)

#Insert the path to the file
#Items in the file go onto one line which the program then splits into individual sections
line = open("/Users/nathan/Documents/CAS-Snake-Program/Programs/adjectives.txt").readline().split()

randWord = line[randNum]

print(randNum)
print(randWord)
print("The bear is " + randWord)
