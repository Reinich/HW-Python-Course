# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

from random import randint
x = randint(2, 10)
y = randint(2, 10)
print(x)
print(y)
print(f'Угадай два числа.\nПодсказки: сумма чисел равна = {x+y}, а произведение = {x*y}. Удачи!')
print()
num_1 = int(input('Первое число: '))
while (num_1 != x) and (num_1 != y):
    print('Неверно! Подумай еще: ')
    num_1 = int(input())
else:
    num_2 = int(input('Второе число: '))
    while (num_2 == num_1) and (x != y):
        print('Неверно! Подумай еще: ')
        num_2 = int(input())
    while (num_2 != x) and (num_2 != y):
        print('Неверно! Подумай еще: ')
        num_2 = int(input())
    if (num_2 == x and num_1 == y) or (num_1 == x and num_2 == y):
        print('Умница! Все верно!')
