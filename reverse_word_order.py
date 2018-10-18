
# def letters_reversed():
#     backwords = input("Give me several words: ")
#     return backwords[::-1]

# print(letters_reversed())

##########

def words_reversed():
    backwords = input("Give me several words: ").split(' ')
    return ' '.join(backwords[::-1])

print(words_reversed())



##########

def reverseWord(w):
    return ' '.join(w.split()[::-1])

print(reverseWord('totally cool'))