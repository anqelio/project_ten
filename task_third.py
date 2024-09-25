try:
    s = input('Введите строку: ').replace(' ', '')
    numbers = "0123456789"
    different_numbers = ''
    not_different = ''
    for i in range(len(s)):
        if s[i].isdigit():
            different_numbers += s[i]
    for i in range(len(numbers)):
        if numbers[i] not in different_numbers:
            not_different+=numbers[i]
    print(not_different)
except ValueError as e:
    print('Некорректный ввод')