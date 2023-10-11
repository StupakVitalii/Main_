variable = 1

variaBle = 2
_Variable = 3

var_number = 4
var_number1 = 5

_var_numb100 = 100

num_1 = float(input('Введіть перше число : '))
num_2 = float(input('Введіть друге число : '))

if num_1 > num_2:
    print(num_1, 'більше ніж ', num_2)
    if num_1 == 0 and num_2 == 0 or num_1 == 0 and num_2 != 0 or num_1 != 0 and num_2 == 0:
        print('При введенні використано число 0 ')
elif num_1 < num_2:
    print(num_1, 'менше ніж ', num_2)
elif num_1 == num_2:
    print('числа рівні')
else:
    print('other')

num3 = float(input('Введіть значення числа 1 : '))
operator = input('Введіть дію з переліку: \n'
                 'додавання (+), віднімання (-) \n'
                 ', множення (*), ділення (/)\n ')
num4 = float(input('Введіть значення числа 2 : '))

if num4 == 0 and operator == '/':
    print('Ділення на 0 неможливе!')
elif operator == '/':
    print('Результат буде : ', num3 / num4 )
elif operator == '+':
    print(num3 + num4)
elif operator == '-':
    print(num3 - num4)
elif operator == '*':
    print(num3 * num4)
