import keyword
s = input()
a = 0
valid = True
lst = ['!', '"', '#', '$', '%', '&', "'",' ', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~']
for i in s:
    if i in lst or i.isupper():
        valid = False
        break
    elif s in keyword.kwlist:
        valid = False
        break
    elif s[0].isdigit():
        valid = False
        break
    # elif s.isnumeric(): #не имеет смысла из за проверки первого символа
    #     print("false")
    #     break
    elif i.isdigit():
        continue
    elif i == '_':
        a += 1
        if a > 1:
            valid = False
            break
    elif not i.isalpha():
        valid = False
        break
    else:
        a = 0
print(valid)












