# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

print('Введите число')
k = int(input())
i = 0
fib = []
fib.append(0)
fib.append(1)
for i in range(k-1): fib.append(fib[i]+fib[i+1]) 
for i in range(k-1): fib.insert(i, fib[-(i+1)]*-1)
print(fib)
