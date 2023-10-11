command = str(input('Введіть ім\'я користувача : '))

match command:
    case 'Dmytro' | 'dmytro' | 'dima' | 'Dima':
        print('Hi Dmytro')
    case 'Petro' | 'petro':
        print('Hello Petro')
    case 'Oksana' | 'oksana':
        print('Hi Oksana')
    case _:
        print('I don\'t understand you')

if command in ('Dmytro', 'dmytro', 'dima'):
    print('Hi Dmytro')
elif command in ('Oksana', 'oksana'):
    print('Hi Oksana')
elif command in ('Petro', 'petro'):
    print('Hello Petro')
else:
    print('I don\'t understand you')
