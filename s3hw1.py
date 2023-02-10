# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random 
my_list = []
print('Введите длину списка, кторый хотите создать')
k = int(input())
for i in range(k): 
    rnd = random.randrange(-100, 101)
    my_list.append(rnd)
print(my_list)
s = 0
for i in range(1, k , 2): 
    s += my_list[i]
print(s)
