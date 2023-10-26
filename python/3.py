# Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
# площадь квадрата и диагональ квадрата.
import math

def square(side):
    if side <= 0:
        raise ValueError("Длина стороны должна быть положительным числом.")
    p = side * 4
    s = side ** 2
    diag = math.hypot(side, side)
    info = (p, s, diag)
    return info


y = input('Введите сторонону квадарата:')
y = int(y)
try:
    result = square(y)
except ValueError as e:
    print(f"Исключение: {e}")
else:
    print(f"Результат: {result}")