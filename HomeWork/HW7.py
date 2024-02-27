my_list = [0, 1, 0, 12, 3]
#my_list = [0]
#my_list = [1, 0, 13, 0, 0, 0, 5]
#my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
for i in range(len(my_list) -1, -1, -1):
    if my_list [i] == 0:
        my_list.append(my_list.pop(i))
print(my_list)