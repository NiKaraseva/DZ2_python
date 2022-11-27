# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

from random import randint as rnd

print('Введите размер списка size: ')
size = int(input())

rnd_list = []

for i in range(size):
    rnd_list.append(rnd(1, 10))

print(*rnd_list)

def mix_list(rnd_list):
    new_list = rnd_list[:]
    for i in range(len(rnd_list)):
        rnd_index = rnd(0, len(rnd_list) - 1)
        temp = new_list[i]
        new_list[i] = new_list[rnd_index]
        new_list[rnd_index] = temp
    return new_list

final_list = mix_list(rnd_list)

print(*final_list)