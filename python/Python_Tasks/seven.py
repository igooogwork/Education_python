# Написать функцию date, принимающую 3 аргумента — день,
# месяц и год. Вернуть True, если такая дата есть в нашем
# календаре, и False иначе.

def is_year_leap(year):
        if year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 != 0:
            return True
        return False

def date(day,month,year):
    calendar = {1:31,
                2:29 if is_year_leap(year) else 28,
                3:31,
                4:30,
                5:31,
                6:30,
                7:31,
                8:31,
                9:30,
                10:31,
                11:30,
                12:31}
    if 1 <= month <= 12 and 1 <= day <= calendar[month]:
        return True
    return False 

input_data = input("Введите дату в виде'12.12.1212':")
data_list = input_data.split ('.')
day, month, year = map(int, data_list)
result = date(day, month, year)
print(result)