my_list=[12,3,4,10]
#my_list=[1]
#my_list=[]
#my_list=[12, 3, 4, 10, 8]
if len(my_list) > 1:
    my_list[-1], my_list[0] = my_list[0], my_list[-1]
    print(my_list)
else: print(my_list)