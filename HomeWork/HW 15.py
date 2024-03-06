while True:
    d = int(input('введіть число від 0 до 8640000:'))
    if d >= 0 and d <= 8640000:
        break
    else:print('некоректне число!!!')

sec, d = d % 60, d // 60
minute, d = d % 60, d // 60
hour, d = d % 24, d // 24
d = str(d)

if d[-1] == '1':
    print(d,' день,', str(hour).zfill(2),':', str(minute).zfill(2),':', str(sec).zfill(2))
elif d[-1] == '2' or d[-1] == '3' or d[-1] == '4':
    print(d,' дні,', str(hour).zfill(2),':', str(minute).zfill(2),':', str(sec).zfill(2))
else:print(d,' днів,', str(hour).zfill(2),':', str(minute).zfill(2),':', str(sec).zfill(2))