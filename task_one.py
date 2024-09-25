try:
    s = input('Введите строку: ').replace(' ', '')
    result = ''
    for item in s:
        if item.isdigit() and result.count(item) == 0:
            result += item
    print(f'{result}')
except ValueError as e:
    print('Некорректный ввод')