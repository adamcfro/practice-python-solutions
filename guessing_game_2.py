# from random import randint
# import time


# secret_number = int(input("Input secret number: "))

# print("Computer, guess my number.")
# comp_guess = 50
# max_num = 100
# min_num = 1
# guesses = 1

# while comp_guess != secret_number:
#     guesses += 1
#     print(comp_guess)
#     if comp_guess > secret_number:
#         print("Guess lower.")
#         time.sleep(1)
#         max_num = comp_guess
#         comp_guess = randint(min_num, max_num - 1)
#     else:
#         print("Guess higher.")
#         time.sleep(1)
#         min_num = comp_guess
#         comp_guess = randint(min_num + 1, max_num)

# print(f"Got the secret number {secret_number} in {guesses} guesses!")


##################

lowest = 0
highest = 100
guess = 50
counter = 1

print("\nComputer, guess the number I'm thinking of.")
condition = input(f"Computer guesses {guess}. Is this number right, human? * * * ")
while condition != 'yes'.lower():
    counter += 1
    if condition == 'lower':
        highest = guess - 1
    elif condition == 'higher':
        lowest = guess + 1
    guess = int((lowest + highest) / 2)
    condition = input(f"Computer guesses {guess}. Is this number right, human? * * * ")
print(f"Good job computer! It took you {counter} guesses!")


