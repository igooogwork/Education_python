# Напишите программу, которая выводит на экран
# числа от 1 до 100. При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz», а вместо чисел,
# кратных пяти — слово «Buzz». Если число кратно и 3, и 5,
# то программа должна выводить слово «FizzBuzz»
count = 1 
while count <=100: 
    comvar = count % 3 
    comvar2 = count % 5 
    if comvar == comvar2 == 0: 
        print('FizzBuzz') 
    elif comvar == 0: 
        print('Fizz') 
    elif comvar2 == 0: 
        print('Buzz') 
    else: 
        print(count) 
    count += 1