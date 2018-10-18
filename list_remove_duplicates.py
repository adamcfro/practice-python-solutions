first = [1, 2, 3, 4, 5, 1, 4, 5, 1, 3, 2, 6, 3, 3, 6]

first = list(set(first))
print(first)

#######

def rem_dups(lst):
    return list(set(lst))

print(rem_dups([1, 2, 3, 4, 5, 1, 4, 5, 1, 3, 2, 6, 3, 3, 6]))

#######

def remove_dupes(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

print(remove_dupes([1, 2, 3, 4, 5, 1, 4, 5, 1, 3, 2, 6, 3, 3, 6]))