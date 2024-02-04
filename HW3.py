# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# from random import randint
# x = int(input("Введите число x: "))
# N = int(input("Введите количество чисел в массиве: "))
# array = []
# for i in range(1, x + 1):
#     array.append(i)
#     print(array[i-1], end = ' ')
#     print()
#     y = int(input())
#     print(array.count(y))



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


# n = int(input())
# lst = [int(input()) for i in range(n)]
# x = int(input())
# min_range = abs(x-lst[0])
# el = lst[0]
# for i in lst:
#     if abs(x-i)<min_range:
#         min_range = abs(x-i)
#         el = i
# print(el)




# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

# Вадим


# N = input('Введите слово: ').upper()
# summ = 0
# dictionary = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#                 'D': 2, 'G': 2,
#                 'B': 3, 'C': 3, 'M': 3, 'P': 3,
#                 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#                 'K': 5,
#                 'J': 8, 'X': 8,
#                 'Q': 10, 'Z': 10,
#                 'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#                 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#                 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#                 'Й': 4, 'Ы': 4,
#                 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#                 'Ш': 8, 'Э': 8, 'Ю': 8,
#                 'Ф': 10, 'Щ': 10, 'Ъ': 10}
# for i in N:
#     summ += dictionary[i]
# print(summ)


# Артур

# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = input().upper()
# count = 0
# if word[0] in "QWERTYUIOPASDFGHJKLZXCVBNM":
#     for sym in word:
#         for key in points_en:
#             if sym in points_en[key]:
#                 count += key
# else:
#     for sym in word:
#         for key in points_ru:
#             if sym in points_ru[key]:
#                 count += key
# print(count)

