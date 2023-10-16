def season(number):
    month = ['Jenuary', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October',
               'November', 'December']
    if number == 1:
        print(month[0])
    elif number == 2:
        print(month[1])
    elif number == 3:
        print(month[2])
    elif number == 4:
        print(month[3])
    elif number == 5:
        print(month[4])
    elif number == 6:
        print(month[5])
    elif number == 7:
        print(month[6])
    elif number == 8:
        print(month[7])
    elif number == 9:
        print(month[8])
    elif number == 10:
        print(month[9])
    elif number == 11:
        print(month[10])
    elif number == 12:
        print(month[11])
    else:
        print('Місяця з таким номером не існує !')
    return ('')

func_2 = season(8)
print(func_2)
