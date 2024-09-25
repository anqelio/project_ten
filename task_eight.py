try:
    count = 0
    s = input('Введите строку: ').replace(' ', '')
    pattern = '.,;:!?'
    for item in s:
        if item in pattern:
            count += 1
    print(f'{count}')
except ValueError as e:
    print('Некорректный ввод')