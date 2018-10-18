number = int(input("Give me a number: "))
if number % 4 == 0:
    print(f"{number} is divisible by 4!")
elif number % 2 == 0:
    print(f"{number} is even!")
else:
    print(f"{number} is odd!")


num, check = input("Give me two numbers: ").split()
num = int(num)
check = int(check)
if num % check == 0:
    print(f"{num} is evenly divisible by {check}!")
else:
    print("Those numbers don't divide evenly.")
