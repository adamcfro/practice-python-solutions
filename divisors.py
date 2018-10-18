number = int(input("Give me a number: "))
for item in range(1, number):
    if number % item == 0:
        print(item)