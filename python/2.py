year = input('Введите год:')
year = int(year)
leap_year = year % 4
if leap_year == 0:
    print('Год високосный')
else:
    print('Год невисокосный') 