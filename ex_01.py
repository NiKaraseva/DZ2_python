# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

print('Введите вещественное число: ')
number = input()

number = number.replace('.', '')

my_list = []
for i in number:
    my_list.append(i)


Sum = 0
for i in range(len(my_list)):
    Sum += int(my_list[i])

print(f'Сумма элементов введённого числа = {Sum}')
