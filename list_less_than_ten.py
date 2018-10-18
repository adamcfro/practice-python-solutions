a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list = []
for item in a:
    if item < 5:
        new_list.append(item)

print(new_list)

number = int(input("give me a number: "))
new_list = []
for item in a:
    if item < number:
        new_list.append(item)

print(new_list)