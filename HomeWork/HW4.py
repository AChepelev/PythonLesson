
while True:
    a = int(input("Введіть перше число:"))
    b = int(input("Введіть друге число:"))
    x = input("Оберіть операцію (+,-,*,/):")
    if x == '+':
        print(a+b)
    elif x == '-':
        print(a-b)
    elif x == '*':
        print(a*b)
    elif x == '/':
        if b != 0:
            print(a/b)
        else: print("На нуль ділити не можна!")
    c = input('Бажаєте здійснити ще одну калькуляцію:(так?/ні)')
    if c.lower() == 'так':
         continue
    else:
        break




