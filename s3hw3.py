# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

print('Введите длину списка, кторый хотите создать')
k = int(input())
my_list = []
new_list = []
b = []
for i in range(k): 
    print('Введите число')
    my_list.append(input())
for i in range(len(my_list)):  
    a = str(my_list[i])
    a = a.split('.')
    b.append(a[1])
for i in range(len(b)):
    for j in range(len(b)):
        if len(b[i])<len(b[j]): b[i] = b[i] + '0'
        print(b[i], b[j])
max = int(b[0])
min = int(b[0])
for i in b:
    if int(i)>int(max): max = int(i)
    elif int(i)<int(min): min = int(i)
print(f'Разница между максимальной и минимальной дробной частью: {max-min}')
