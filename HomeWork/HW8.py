#lst =[1, 3, 5]
#lst = [6]
lst = []
mul = 0
for i in range(0,len(lst),2):
    mul += lst[i]*lst[-1]
print(mul)