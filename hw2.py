# Задание 1 Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
num = str(input("Введите число: "))
sum = 0
for i in num:
    if i.isdigit():
        sum = sum + int(i)
print("Сумма цифр числа равна: ", sum)

# Задание 2 Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
n = int(input("Введите число: "))
p=1
a = [p:=p*i for i in range(1, n+1)]
print(a)

# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n 
# и выведите на экран их сумму, округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072

# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.
n = int(input("Введите число: "))
list = list(range(-n, n))
print(list)

a = int(input("введите позицию a: "))
b = int(input("введите позицию b: "))

print(list[a] * list[b])

# Задание 5 Реализуйте алгоритм перемешивания списка.
import random
n = input("Введите список:\n")
n = list(n)
a = random.sample(n,  len(n))
print(a)

# Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Пример
# Для "abababb" и "aba" -> 2
a = 'abababb'
i = 1
count = 0
b = 'aba'
while i != -1:
    i = a.find(b)
    if i >= 0:
        count += 1
    a = a[i+1:]
print(count)
