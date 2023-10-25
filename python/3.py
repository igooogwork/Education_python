# Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
# площадь квадрата и диагональ квадрата.
side_of_a_square = input('Введите величину стороны квадрата:')
side_of_a_square = int(side_of_a_square)
perimeter_of_a_square = side_of_a_square * 4
area_of_the_square = side_of_a_square ** 2
diagonal_of_a_square = side_of_a_square * (2 ** 0.5)
square = (perimeter_of_a_square, area_of_the_square, diagonal_of_a_square)
print(square)