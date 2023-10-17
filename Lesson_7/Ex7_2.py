def season(number):
    month = ['Winter', 'Spring', 'Summer', 'Autumn']
    if number in range(1, 3) or number == 12:
        print(month[0])
    elif number in range(3, 6):
        print(month[1])
    elif number in range(6, 9):
        print(month[2])
    elif number in range(9, 12):
        print(month[3])
    else:
        print('Місяця з таким номером не існує !')
    return ('')

func_2 = season(12)
print(func_2)
