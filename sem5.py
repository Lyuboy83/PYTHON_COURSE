# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input('Введите число n: '))

# fibonacci_array = [fibonacci(n) for _ in range(n)]
# print(f'{n} число Фибоначчи равняется {fibonacci_array[n-1]}')




# 10:30
# Александр Карпекин
# # N = abs(int(input('Input: ')))
# # def f(n):
# #     if n <= 1:
# #         return 1
# #     else:
# #         return f(n-1) + f(n-2)
# #
# # print(f'Output: {f(N)}')

# 10:33
# Юрий Тарасевич
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# n = int(input('Введите номер числа Фибоначчи: '))
# print(fibonacci(n))

# 10:33


# from random import randint
# n = 5
# li1 = [randint(1, 5) for i in range(n)]
# print(f'Input: {n} ->', *li1)
# li2 = sorted(li1)

# def merge_two_lists(a, b):
#     c = []
#     i = j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#     if i < len(a):
#         c += a[i:]
#     if j < len(b):
#         c += b[j:]
#     return c


# def merge_sort(li):
#     if len(li) == 1:
#         return li
#     middle = len(li) // 2
#     left = merge_sort(li[:middle])
#     right = merge_sort(li[middle:])
#     return merge_two_lists(left, right)


# for i in range(len(li1)):
#     if li1[i] == li2[len(li1)-1]:
#         li1[i] = li2[0]
# print('Output:', *li1)

# '''Если divisor в квадрате больше числа n,
# это означает, что все делители уже были проверены,
# и число считается простым, и функция возвращает True.
# В противном случае, функция вызывает саму себя,
# увеличивая значение divisor на 1, и продолжает проверку.'''


# def simple(n, divisor=2):
#     if n <= 1:
#         return False
#     elif n == 2:
#         return True
#     elif n % divisor == 0:
#         return False
#     elif divisor * divisor > n:
#         return True
#     else:
#         return simple(n, divisor + 1)

#     num = abs(int(input('Input: ')))
# print('yes' if simple(num) else 'no')


# 37


# 10:46
# from random import randint
# n = 5
# li1 = [randint(1, 5) for i in range(n)]
# print(f'Input: {n} ->', *li1)
# li2 = li1[::-1]
# print(*li2)


# # Вариант 2

# li1 = '63324289329'
# print(f'Input: {li1}')
# li2 = li1[::-1]
# print(li2)


# Задача с кустами и грядками

# from random import randint
# N = int(input('Сколько кустов?: '))
# li = [randint(1,3) for i in range(N)]
# print(*li)
# maximum = 0
# for i in range(N):
#     summa = li[i-2] + li[i-1] + li[i]
#     if summa > maximum:
#         maximum = summa
# print(maximum)


# Задача №112288. Симметричные пары
# Пара элементов в массиве называется симметричной , если эти элементы находятся на одинаковом расстоянии
# от концов массива. Так в массиве размером N симметричными будут пары элементов
# с порядковыми номерами 1 и N , 2 и N - 1 и т.д. (при нумерации с единицы).
# Напишите программу, которая заполняет массив из N элементов случайными целыми числами
# в диапазоне [ A , B ] и определяет номера двух симметричных элементов этого массива, сумма которых
# чётная и максимальная среди всех пар симметричных элементов. Если ни одной такой пары нет, нужно
# вывести два нуля. Если есть несколько таких пар, нужно вывести номера элементов, составляющих пару,
# ближайшую к центру массива.

# Входные данные
# Входная строка содержит три числа: границы диапазона случайных чисел A и B , а также размер массива N .
# Все числа разделены пробелами. Гарантируется, что 0 < N ≤ 10000 .

# Выходные данные
# В первой строке программа должна вывести N элементов построенного массива, разделив их пробелами, а
# во второй строке – номера двух симметричных элементов массива, имеющих максимальную чётную сумму.
# Если ни одной такой пары нет, нужно вывести два нуля.

# Примеры
# входные данные
# 10 20 10
# выходные данные
# 10 10 19 12 13 17 13 11 14 14
# 5 6
# '''
