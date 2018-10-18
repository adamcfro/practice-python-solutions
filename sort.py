def finder(lst, num):
    my_list = lst
    target = num
    guess = 0
    counter = 1
    print(my_list)  ## not necessary
    while not (len(my_list) == 1 or guess == target):
        counter += 1
        center_index = int(len(my_list) / 2)
        guess = my_list[center_index]
        if guess > target:
            my_list = my_list[:center_index]
            print(my_list)  ## not necessary
        elif guess < target:
            my_list = my_list[center_index:]
            print(my_list)  ## not necessary

    if guess == target:
        print(f"Found target! Guess = {guess}. {counter} tries.")
    else:
        print(f"Target not found. Last guess = {guess}. {counter} tries.")

finder([-10, 1, 2, 6, 7, 12, 21], 12)
finder([-10, 2, 3, 6, 11, 12, 21], 11)