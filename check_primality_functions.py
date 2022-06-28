def get_number():
    """
    This function takes in a number and returns a string stating whether or not
    the number is prime.
    """
    number = int(input("Give me a number: "))
    for num in range(2, number - 1):
        if number % num != 0:
            return "The number is prime"
        elif number % num == 0:
            return "The number is not prime"


print(get_number())