from collections import Counter

with open('read_from_file_names.txt', 'r') as file:
    content = file.read()

names = dict(Counter(content.split()))

for k, v in names.items():
    print(f"{k} appears {v} times.")

# print(names)
