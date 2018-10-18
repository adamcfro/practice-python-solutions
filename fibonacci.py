def fib_nums():
    new_nums = 'yes'
    while new_nums == 'yes':
        number = int(input("How many Fibonacci numbers would you like to generate?: "))
        a = 0
        b = 1
        for num in range(1, number + 1):
            print(a)
            a, b = b, a + b
        new_nums = input("More nums? (yes or no) ")

fib_nums()