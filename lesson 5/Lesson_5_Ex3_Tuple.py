#Ex_3a,b
print('Ex_3(a,b)\n'
      'Створити кортеж котрий приймає в себе наступний ряд: 1, 2, 3, 4, 5, 6, 7: \n')

_tup_1a = (1, 2, 3, 4, 5, 6, 7)
print(_tup_1a)
print(type(_tup_1a), '\n')

#Ex_3c
print('Ex_3(c)\n'
      'Створити кортеж кортежів: \n')
_tup_3c = (0, 9, 8, 7, 6)
_tup_3c1 = _tup_1a, _tup_3c
print('Tuple 1 :', _tup_1a)
print('Tuple 2 :', _tup_3c)
print('Tuple of tuples :', _tup_3c1)
print(type(_tup_3c1), '\n')

#Ex_3d
print('Ex_3(d)\n'
      'Розширити кортеж через приведення типів: \n')

_tup_3c1 = list(_tup_3c1)
print(_tup_3c1)
print(type(_tup_3c1), '\n')
_tup_3c1.append((1, 3, 155))

_tup_3c1 = tuple(_tup_3c1)
print('Result : ', _tup_3c1)
print(type(_tup_3c1), '\n')
