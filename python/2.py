# Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.
year = input('Введите год:')
year = int(year)
leap_year = year % 4
if leap_year == 0:
    is_year_leap = True
    print(is_year_leap)
else:
    is_year_leap = False
    print(is_year_leap)