#Ex_2(a)
import copy

print('Ex_2(a)\n'
      'Створити set котрий приймає в себе наступний ряд: 1, 2, 3, 4, 5, 6, 7: \n')

_set_1a = {1, 2, 3, 4, 5, 6, 7}
print('SET =',_set_1a)
print('SET type :', type(_set_1a), '\n')

#Ex_2(b)
print('Ex_2(b)\n'
      'Створити set котрий приймає в себе наступний ряд: 5, 6, 7, 8, 9, 10, 11: \n')
_set_1b = copy.deepcopy(_set_1a)
_set_1b.clear()
_set_1b.update({5, 6, 7, 8, 9, 10, 11})
print(_set_1b)
print(type(_set_1b), '\n')

#Ex_2(c)
print('Ex_2(c)\n'
      'Розширити перший сет за допомогою комaнди .add(0): \n')
_set_1a.add(100)
print(_set_1a, '\n')

#Ex_2(d)
print('Ex_2(d)\n'
      'Виконати команду .intersection() на першому сеті передаючи в команду другий сет як аргумент,\n'
      ' результат зберегти у нову змінну: \n')

_set_2d = _set_1a.intersection(_set_1b)
print(_set_2d, '\n')

#Ex_2(e)
print('Ex_2(e)\n'
      'Виконати команду .difference() на першому сеті передаючи в команду другий сет як аргумент,\n'
      ' результат зберегти у нову змінну.\n')

print('Перший сет :', _set_1a)
print('Другий сет :', _set_1b)
_set_2e = _set_1a.difference(_set_1b)
print('Результат', _set_2e, '\n')

#Ex_2(f)
print('Ex_2(f)\n'
      'Виконати команду .symmetric_difference() на першому сеті передаючи в команду другий сет як аргумент,\n'
      ' результат зберегти у нову змінну.\n')

print('Перший сет :', _set_1a)
print('Другий сет :', _set_1b)
_set_2f = _set_1a.symmetric_difference(_set_1b)
print('Результат', _set_2f, '\n')

print('SET 1 : ', _set_1a)
print(type(_set_1a), '\n')
print('SET 2 : ', _set_1b)
print(type(_set_1b))
print('Result : ', _set_2d)
print(type(_set_2d))
print('Result : ', _set_2e)
print(type(_set_2e))
print('Result : ', _set_2f)
print(type(_set_2f), '\n')
