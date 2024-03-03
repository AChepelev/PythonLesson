#при удалении знаков пунктуации делал след. букву заглавной
#print('#' + ''.join(filter(str.isalnum, input().title()))[:139])

str = input("Введіть рядок: ")

a = ''.join(i.capitalize() for i in str.split())
b = ''.join(i for i in a if i.isalnum())
hashtag = b

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print('#', hashtag, sep='')