import keyword
import string

name = input("Введіть ім'я змінної: ")

if name == "_":
    print(True)
    exit()
elif name in keyword.kwlist:
    print(False)
    exit()
elif name[0].isdigit():
    print(False)
    exit()
elif name.isdigit():
    print(False)
    exit()

for char in name:
    if char.isupper() or char in string.punctuation.replace("_", "") or char == " ":
        print(False)
        exit()

print(True)




