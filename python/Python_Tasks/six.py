# Написать функцию is_prime, принимающую 1 аргумент — число
# т 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
import sys

def contains_digit(number):
    return all(char.isdigit() for char in str(number))
    
def is_prime(number):
    if number < 2 or number > 1000:
        return False
    sieve = [True] * (1001) 
    sieve[0] = sieve[1] = False
    for p in range(2, int(number**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, 1001, p):
                sieve[i] = False
    return sieve[number]

number_to_check = input('Введите число:')

if contains_digit(number_to_check):
    number_to_check = int(number_to_check)
else:
    print("Программа завершена - некорректный ввод")
    sys.exit(1)
    
if is_prime(number_to_check):
    print(f"{number_to_check} - простое число")
else:
    print(f"{number_to_check} - не простое число")    
