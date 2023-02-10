# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_list = []
power_list = []
print('Введите длину списка, кторый хотите создать')
k = int(input())
for i in range(k): 
    print('Введите число')
    my_list.append(int(input()))
if k%2 == 0: k-=1
for i in range(round(k/2)+1):
    power_list.append(my_list[i]*my_list[-(i+1)])
print(my_list)
print(power_list)
