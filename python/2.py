# Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.
year = input('Введите год:')
year = int(year)
if year % 4 == 0:
    is_year_leap = True
    print(is_year_leap)
else:
    is_year_leap = False
    print(is_year_leap)