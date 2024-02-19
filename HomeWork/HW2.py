number = int(input("Введите число:"))

# Вариант 1
x = 100
x2 = 10
a, b = divmod(number, x)
c, d = divmod(a, x2)
f, e = divmod(b, x2)
print(c)
print(d)
print(f)
print(e)

# Вариант 2
#x = 10
#a, b = divmod(number, x)
#c, d = divmod(a, x)
#f, e = divmod(c, x)
#print(f)
#print(e)
#print(d)
#print(b)

# Сокращение с использованием сепаратора
#print(f, e, d, b, sep='\n')
