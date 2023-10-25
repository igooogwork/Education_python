# Написать функцию arithmetic, принимающую 3 аргумента:
# первые 2 - числа, третий - операция, которая должна 
# быть произведена над ними. Если третий аргумент +, сложить их;
# если —, то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях вернуть строку "Неизвестная операция".
first_number = input('Введите первое число:')
second_number = input('Введите второе число:')
operation = input('Введите тип(+ , - , * , /) операции:')
first_number = int(first_number)
second_number = int(second_number)
if operation == '+':
    arithmetic = first_number + second_number
    print(arithmetic)
elif operation == '-':
    arithmetic = first_number - second_number
    print(arithmetic)
elif operation == '*':
    arithmetic = first_number *second_number
    print(arithmetic)
elif operation == '/':
    arithmetic = first_number / second_number
    print(arithmetic)
else:
    print('Неверный тип операции')