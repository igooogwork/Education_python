# Написать функцию is_prime, принимающую 1 аргумент — число
# т 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
is_prime = input('Введите число от 0 до 1000:')
if str.isdigit(is_prime):
    is_prime = int(is_prime)
    while not 0 <= is_prime <= 1000:
        is_prime = input('Введите число от 0 до 1000:')
        is_prime = int(is_prime)
    is_prime = True
    print(is_prime)
else:
    is_prime = False
    print(is_prime)