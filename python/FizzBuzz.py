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