def take_in(lst, num):
    if num in lst:
        return True
    return False

print(take_in([1, 2, 3, 4], 4))
print(take_in([1, 2, 3, 4], 5))
