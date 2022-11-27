# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.

from decimal import Decimal

print('Введите число N: ')
N = int(input())

my_list = []
Sum = 0
for i in range(N):
    while N > 0:
        my_list.append(Decimal(str((1 + 1/N) ** N)))
        Sum += round(my_list[i], 2)
        N -= 1

my_list.reverse()
print(*my_list)
print(f'Сумма элементов введённого числа = {Sum}')
