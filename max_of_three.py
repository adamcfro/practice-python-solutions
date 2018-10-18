def three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c

print(three(1, 2, 3))
print(three(17, 9, 11))