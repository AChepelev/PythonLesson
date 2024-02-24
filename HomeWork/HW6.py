my_list=[12,3,4,10]
#my_list=[1]
#my_list=[]
#my_list=[12, 3, 4, 10, 8]
if len(my_list) > 1:
    a = my_list.pop(-1)
    my_list.insert(0,a)
    print(my_list)
else: print(my_list)