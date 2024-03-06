import string

row_of_letters = string.ascii_letters

range = list(input('введіть через дефіс дві літери:'))

point_1 = range[0]
point_2 = range[2]

result = row_of_letters[row_of_letters.find(point_1):row_of_letters.find(point_2)+1]

print(result)
