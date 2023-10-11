#Ex_1(a)
import copy

print('Ex_1(a)\n'
      'Пустий словник : \n')

_dict_1a = {}
print(type(_dict_1a))

#Ex_1(b)
print('Ex_1(b)\n'
      'Створити новий словник з 2-3 парами ключ:значення : \n')

_dict_1b = {'Ukraine': "Kyiv",
            'UK': 'London',
            'Germany': 'Berlin'}
print(_dict_1b, '\n')
print(_dict_1b['Ukraine'], '\n')

#Ex_1(c)
print('Ex_1(c)\n'
      'Додати одну пару ключ:значення до першого словника : \n')

print(_dict_1a)
_dict_1a.update({'Poland': 'Warsawa', 'France': 'Paris'})
print(_dict_1a, '\n')

#Ex_1(d)
print('Ex_1(d)\n'
      'Додати до першого словника другий словник використовуючи .update(): \n')
print(_dict_1a)
_dict_1a.update(_dict_1b)
print(_dict_1a, '\n')

#Ex_1(e)
print('Ex_1(e)\n'
      'Видалити один елемент словника за допомогою .pop(): \n')
_dict_1e = copy.deepcopy(_dict_1a)
print(_dict_1e)
_dict_1e.pop('UK')
print(_dict_1e,'\n')

#Ex_1(f)
print('Ex_1(f)\n'
      'Видалити один елемент за допомогою .popitem(): \n')

print(_dict_1e)
_dict_1e.popitem()
print(_dict_1e, '\n')

#Ex_1(g)
print('Ex_1(g)\n'
      'Зробити глибоку копію першого словника в нову змінну: \n')
print(_dict_1a)
_dict_1g = copy.deepcopy(_dict_1a)

#Ex_1(h)
print('Ex_1(h)\n'
      'Додати до нового словника новий ключ, а як значення передати перший словник: \n')

_dict_1h = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
print('Новий словник :\n', _dict_1h, '\n')
_dict_1h.update({5: _dict_1a})

print('Перший словник :\n', _dict_1a)
print('Результат додавання :\n', _dict_1h, '\n')

#Ex_1(i)
print('Ex_1(i)\n'
      'Вивести список ключів : \n')
print(_dict_1h.keys())

#Ex_1(j)
print('Ex_1(j)\n'
      'Вивести список значень : \n')

print(_dict_1h.values())