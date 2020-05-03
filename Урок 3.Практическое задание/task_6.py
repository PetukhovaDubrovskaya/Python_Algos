"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""
import random

n = int(input('Введите количество элементов в массиве: '))
a = []
for i in range(0, 100):
    a.append(i)
random.shuffle(a)
b = a[:n]
print(b)

for idx, i in enumerate(b):
    if i == max(b):
        k = idx
    elif i == min(b):
        j = idx

if k < j:
    print(f'Сумма элементов между максимальным значением {max(b)} и минимальным значением {min(b)} равна {sum(b[k + 1 : j])}')
else:
    print(f'Сумма элементов между минимальным значением {min(b)} и максимальным значением {max(b)} равна {sum(b[j + 1 : k])}')








