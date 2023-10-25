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