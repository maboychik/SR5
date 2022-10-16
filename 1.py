num = int(input('Введите число: '))
base = int(input('Введите целевую систему счисления: '))


def num_base(num, base):
    new_num = ''
    while num > 0:
        new_num = str(num % base) + new_num
        num = num // base
    return int(new_num)


print('Итог:', num, '--->', num_base(num, base))
