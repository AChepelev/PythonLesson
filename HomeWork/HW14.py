user_inp = input('Введіть число:')

while True:
    a = 1
    for i in user_inp:
        a *= int(i)
    if a <= 9:
        break
    user_inp = str(a)
print(a)