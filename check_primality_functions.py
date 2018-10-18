# def get_integer(help_text="Give me a number: "):
#     return int(input(help_text))

# age = get_integer("Tell me your age: ")
# school_year = get_integer("What grade are you in?: ")
# if age > 15:
#     print("You are over 15.")
# print(f"You are in grade {school_year}.")




#################


def get_number():
    number = int(input("Give me a number: "))
    for num in range(2, number - 1):
        if number % num != 0:
            return "The number is prime"
        elif number % num == 0:
            return "The number is not prime"


print(get_number())