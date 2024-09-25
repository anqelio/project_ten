try:
    s = input('Введите строку: ').replace(' ', '')
    if s.isalnum():
        print(len(s)-1)
    else:
        print('NO')
except ValueError as e:
    print('Некорректный ввод')