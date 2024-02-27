import random
my_list = []

for i in range(random.randint(3, 10)):
    my_list.append(random.randint(1, 9))

a = my_list[0]
b = my_list[2]
c = my_list[-2]
new_list = [a, b, c]
print(my_list, '==', new_list)
