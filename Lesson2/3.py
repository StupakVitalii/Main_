
command = str(input('Введіть ім\'я користувача : '))
if command in ('Dmytro', 'dmytro', 'dima'):
    print('Hi Dmytro')
elif command in ('Oksana', 'oksana'):
    print('Hi Oksana')
elif command in ('Petro', 'petro'):
    print('Hello Petro')
else:
    print('I don\'t understand you')