# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую(НЕ ОТРИЦАТЕЛЬНУЮ!!!) степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# a = int(input("Введите основание степени: "))
# b = int(input("Введите показатель степени: "))


# def f(m, n):
#     if n == 1:
#         return m
#     else:
#         return m*f(m, n-1)

# их вариант

# def f(a, b):
#     if b == 0:
#         return 1
#     return f(a, b - 1) * a


# print(f(a, b))

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

# def sum(a, b):
#     if b == 0:
#         return a
#     else:
#         return sum(a, b-1) + 1


# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# print(sum(a, b))