number = 0
total = 0.0

while True:
    sval = input('Enter a number: ')
    
    if sval == 'done':
        break
    
    try:
        fval = float(sval)
    except ValueError:
        print('Invalid input')
        continue

    number = number + 1
    total = total + fval

    print(total, number, total / number)
