from random import randint

guessesTaken = 0
print("Guess a number between 1 and 10")

number = randint(1,10)

while guessesTaken < 6:
    guess = input("Guess my number: ")

    guess = int(guess)
    try:
        if guess == number:
            guessesTaken += 1
            break

        if guess > number:
            print("Too high!")
            guessesTaken += 1

        if guess < number:
            print("Too low!")
            guessesTaken += 1
    except:
        print("Invalid Input")
        guessesTaken += 1

if guess == number:
    if guessesTaken  == 1:
        print("You guessed the number on your first try!")
    else:
        print("You got my number in " + str(guessesTaken) + " guesses")

if guess != number:
    print("")
    print("Too Bad!")
    print("My number was " + str(number))
