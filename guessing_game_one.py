from random import randint

number = randint(1, 9)
guess = int(input("Guess a number between 1 and 9: "))
guesses = 0

if guess == number:
    print("You guessed it first time!")
else:
    guesses += 1
    while guess != number:
        if guess < number:
            guess = int(input("Guess higher: "))
            guesses += 1
        else:
            guess = int(input("Guess lower: "))
            guesses += 1
    print(f"You guessed it in {guesses} guesses!")