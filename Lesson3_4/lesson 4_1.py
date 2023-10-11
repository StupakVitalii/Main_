# Ex1 (a)
import copy

print('Ex1 (a)\n '
      'Навести приклад простого рядка: ', '\n')
_easy_str = 'easy string'
print(_easy_str, '\n')

# Ex1 (b)
print('Ex1 (b)\n'
      'Навести приклад багаторядкового рядка (Вірш, хоку - щоб показати форматування)\n')
_head = (5 * '*' + '  ' + 'Вірш хоку' + '  ' + 5 * '*')
_head_2 = (5 * '*' + '  ''Мацуо Басьо''  ' + 5 * '*')

_hoku = str(' На голій гілці \n '
            'самотній ворон тихо старіє. \n '
            'Осінній вечір. ')

print(_head)
print(_hoku)
print(_head_2, '\n')

# Ex1 (c)
print('Ex1 (c)\n'
      'Навести приклад рядка з ігноруванням екрануючих символів (Raw) :\n')
_raw_string = r'Рядок з ігноруванням екрануючих символів (Raw) :\n'
print(_raw_string, '\n')

# Ex1 (d)
print('Ex1 (d)\n'
      'Навести приклад форматування довгих рядків:\n')

name = input('Enter your name : \n ')
age = input('Your age : \n ')
result_1 = f'Мене звати {name} і мені {age} років'
print(result_1, '\n')

# Ex2_(a)

print('Ex2 (a)\n створити список :\n')
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k']
list_3 = [100, '55', 'alpha']

print('list_1 = ', list_1)
print('list_2 = ', list_2)
print('list_3 = ', list_3, '\n')

# Ex2_(b)
print('Ex2 (b)\n копіювати через .copy() :\n')
_deep_copy_l1 = copy.deepcopy(list_1)
_deep_copy_l2 = copy.deepcopy(list_2)
_deep_copy_l3 = copy.deepcopy(list_3)

print(_deep_copy_l1, '\n')
print(_deep_copy_l2, '\n')
print(_deep_copy_l3, '\n')


#Ex2_(c,d)
print('Ex2_(c,d)\n '
        'Додати елемент до списку. \n '
        'Вставити елемент в  певне місце:\r')
_deep_copy_l11 = copy.deepcopy(_deep_copy_l1)
_deep_copy_l11.insert(3, 0)
print(_deep_copy_l11, " \n ")

# Ex2_(e)
print('Ex2_(e)')
print('Результат додавання списків метод 1 : \r')
_deep_copy_l1.extend(_deep_copy_l2)
print(_deep_copy_l1, '\n')

_deep_copy_l1.append(_deep_copy_l2)

#print(list.__add__([_deep_copy_l1], [_deep_copy_l2]), ' \n')
res_1 = _deep_copy_l1 + _deep_copy_l2 + _deep_copy_l3
print('Результат додавання списків метод 2 : \n' + str(res_1), '\n ')

# Ex2_(f)
print('Ex2_(f)\n'
      'Команда pop()')

_deep_copy_l1_Ex2f = copy.deepcopy(list_1)
_deep_copy_l2_Ex2f = copy.deepcopy(list_2)
_deep_copy_l3_Ex2f = copy.deepcopy(list_3)

_deep_copy_l1_Ex2f.pop(0)
_deep_copy_l2_Ex2f.pop(0)
_deep_copy_l3_Ex2f.pop(0)
print(_deep_copy_l1_Ex2f)
print(_deep_copy_l2_Ex2f)
print(_deep_copy_l3_Ex2f, '\n')

# Ex2_(g)
print('Ex2_(g)\n'
      'Видалити елемент за індексом та за значенням \n')
_deep_copy_l1_Ex2g = copy.deepcopy(list_1)
_deep_copy_l2_Ex2g = copy.deepcopy(list_2)
_deep_copy_l3_Ex2g = copy.deepcopy(list_3)

del _deep_copy_l1_Ex2g[4]
del _deep_copy_l2_Ex2g[4]
del _deep_copy_l3_Ex2g[1]

_deep_copy_l1_Ex2g.remove(6)
_deep_copy_l2_Ex2g.remove('c')
_deep_copy_l3_Ex2g.remove('alpha')

print(_deep_copy_l1_Ex2g)
print(_deep_copy_l2_Ex2g)
print(_deep_copy_l3_Ex2g, '\n')

# Ex2_(h)
print('Ex2_(h)\n'
      'Як дістати значення елемента за індексом : \n')

_deep_copy_l1_Ex2h = copy.deepcopy(list_1)
_deep_copy_l2_Ex2h = copy.deepcopy(list_2)
_deep_copy_l3_Ex2h = copy.deepcopy(list_3)

print(_deep_copy_l1_Ex2h.index(4))
print(_deep_copy_l2_Ex2h.index('f'))
print(_deep_copy_l3_Ex2h.index('alpha'), '\n')

# Ex2_(i)
print('Ex2_(i)\n'
      'Створити змінну з посиланням на перший список : \n')
_deep_copy_l1_Ex2_i = copy.deepcopy(list_1)
print(_deep_copy_l1_Ex2_i, '\n')

# Ex2_(j)
print('Ex2_(j)\n'
      ' Створити поверхову (Shallow copy) копію першого списка: \n')
_shallow_copy_l1_Ex2_j = list_1
print(_shallow_copy_l1_Ex2_j, '\n')

# Ex2_(k)
print('Ex2_(k)\n'
      ' Створити повну копію першого списка: \n')
_deep_copy_l1_Ex2_k = copy.deepcopy(list_1)
print(_deep_copy_l1_Ex2_k, '\n')

# Ex2_(l)
print('Ex2_(l)\n'
      ' Вивести значення всіх списків: \n')
print(list_1)
print(list_2)
print(list_3, '\n')

# Ex2_(m)
print('Ex2_(m)\n'
      ' Змінити перший список і ще раз вивести значення всіх списків: \n')
_copy_l1_Ex2_m = copy.deepcopy(list_1)
_copy_l1_Ex2_m.insert(4,'one million')
print(_copy_l1_Ex2_m)
print(list_1)
print(list_2)
print(list_3, '\n')

#Ex3_(a)
print('Ex3_(a)\n'
        'Тривимірний список :\r')
list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'a', 'a', 'a', 'a']
list_c = [1, '1000', 'сто тисяч']
list_res = [list_a, list_b, list_c]
print(list_res, '\n')

#Ex3_(b)
print('Ex3_(b)\n'
        'Змінити будь який елемент будь якого спику :\r')
_deep_copy_list_a = copy.deepcopy(list_a)
_deep_copy_list_b = copy.deepcopy(list_b)
_deep_copy_list_c = copy.deepcopy(list_c)
_deep_copy_list_a[0:3] = ['10', '10', '10']
_deep_copy_list_b.insert(3,100)
_deep_copy_list_b[0] = 100
_deep_copy_list_c.insert(1,'one thousand')
_deep_copy_list_c[2] = 'abc'
_copy_list_res = [_deep_copy_list_a, _deep_copy_list_b, _deep_copy_list_c]
print(_copy_list_res, '\n')

#Ex3_(c)
print('Ex3_(c)\n'
        'Вивести значення до та після :\r')
print('Значення list_a до : \n ', list_a, ' \n ',
      'Значення list_a після : \n ', _deep_copy_list_a, ' \n')
print('Значення list_b до : \n ', list_b, ' \n ',
      'Значення list_b після : \n ', _deep_copy_list_b, ' \n')
print('Значення list_c до : \n ', list_c, ' \n ',
      'Значення list_c після : \n ', _deep_copy_list_c, ' \n')

#Ex3_(d)
print('Ex3_(d)\n'
        'Створити словник зі вкладеним списком :\n')
_dict_l1_Ex3d = {1: list_1, 2: list_2, 3: list_3}

print(_dict_l1_Ex3d, '\n')

#Ex3_(e)
print('Ex3_(e)\n'
        'Зберегти вкладений список зі словника у нову змінну :\n')

_dict_l1_Ex3e = {1: list_1, 2: list_2, 3: list_3}
new = _dict_l1_Ex3e[1]

print(new, '\n')

#Ex4
print('Ex4 \n',
        'Показати форматування рядків за допомогою "{}".format() та f"{}" :\n')
var_a = 10
var_b = 20
var_sum = '{0} + {1} = {2}'.format(var_a, var_b, var_a + var_b)
print(var_sum)

#Ex5
print('Ex5 \n'
        'Показати роботу методів типу даних Рядок \n '
      '(на приклад .split(), .upper(), .lower(), .capitalize(), .find()*) :\n')

f = 'HOW are YOU'
g = 'how ARE you'
h = 'Good MoRnInG'

print(f.lower())
print(g.upper())
print(h.capitalize())
print(f.split())
print(g.find('R'))

#Ex6(a)
print('Ex6(a) \n'
        'За допомогою даної конструкції перевернути рядок \n ')

var_str = 'abcdefghijklmno'
print(var_str)
print(var_str[::-1], '\n')

#Ex6(b)
print('Ex6(b) \n'
        'За допомогою даної конструкції перевернути рядок \n ')

var_str1 = list(var_str)
print(var_str1)
print(list(reversed(var_str1)))

#Ex6(c)
print('Ex6(c) \n'
        'Повернути частину списку від 2 до 7 елементу з кроком 2 \n ')

print(var_str1[1:7:2], '\n')

#Ex6(d)
print('Ex6(d) \n'
        'Повернути частину рядка (вважати рядок списком) \n ')
var_str_Ex6d = 'abcdefghijklmno'
var_str_Ex6d = list(var_str_Ex6d)

print(var_str_Ex6d[:5], '\n')

#Ex7
print('Ex7 \n'
        'За допомогою циклу for вивести всі елементи списку в консоль \n ')
list_Ex7 = 'sdgnkrgjbnrkgvjbvdv'
list_Ex7 = list(list_Ex7)
for item in list_Ex7, '\n':
    print(item)

#Ex8
print('Ex8 \n'
        'За допомогою циклу While вивести всі елементи списку в консоль \n ')
list_Ex8 = 'sdgnkrgjbnrkgvjbvdv'
list_Ex8 = list(list_Ex8)
while True:
    message = list_Ex8
    print(message)
    break
print('\n')

# Ex9
print('Ex9 \n'
      'За допомогою циклу for створити піщаний годинник :\n ')

print(*[('* ' * i).rjust(7 * 2 + i)
for i in range(15, 1, -2)], *[('* ' * i).rjust(7 * 2 + i)
for i in range(1, 17, 2)], sep='\n')





