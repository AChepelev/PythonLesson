list = [1, 2, 3, 4, 5, 6]
#list = [1, 2, 3]
#list = [1, 2, 3, 4, 5]
#list = [1]
#list = []
x = len(list) - len(list) // 2
list_1 =[list[:x],list[x:]]
print(list_1)