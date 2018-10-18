birthdays = {'Albert Einstein': '05/14/1879', 'Benjamin Franklin': '01/17/1706', 'Ada Lovelace': '12/10/1815'}


print(f"Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthdays:
    print(name)

name = input("Whose birthday do you want to look up? ")
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}.")
else:
    print(f"Sadly, we don't any files for {name}...")

