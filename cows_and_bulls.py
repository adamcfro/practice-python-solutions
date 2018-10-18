from random import randint


def num_generator():
    secret_num = []
    i = 0
    while i < 4:
        num = randint(0, 9)
        secret_num.append(num)
        i += 1
    return secret_num

def cows_and_bulls(func):
    print("\nGuess the secret 4-digit number. For every correct number in the correct position, you get one 'cow'. For every correct number in the wrong postion, you get one 'bull'.")
    guesses = 0
    correct = False
    secret_num = num_generator()
    while not correct:
        guess = list(input("Guess the 4-digit number: "))
        new_list = []
        for item in guess:
            new_list.append(int(item))

        bull = 4
        cow = 0
        for i in range(len(new_list)):
            if new_list[i] == secret_num[i]:
                bull -= 1
                cow += 1
        print(f"bull: {bull}, cow: {cow}")
        guesses += 1
        if new_list == secret_num:
            break
    return f"You guessed the number in {guesses} guesses!"


print(cows_and_bulls(num_generator))
