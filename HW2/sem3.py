# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


# list = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list)))


# list1 = [1, 1, 2, 0, -1, 3, 4, 4]
# list2 = []
# for i in list1:


# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан

# list3 = [1, 2, 3, 4, 5]
# k = 2
# k = k % len(list3)

# list_output = list3[-k:] + list3[:-k]

# print(list3[-k:])
# print(list3[:-k])
# print(list_output)


# def move(lst, steps):
#     if steps > 0:
#         for i in range(steps):
#             lst.insert(0, lst.pop())

# nums = [1, 2, 3, 4, 5]
# print(nums)

# move(nums, 2)
# print(nums)


# list4 = [1, 2, 3, 4, 5]
# # print((list4).pop(2))
# # print(list4.remove(4))
# # print(list4)

# k = 5

# for i in range(5):
#     temp = list4.pop()
#     list4.insert(0, temp)
#     print(list4)


# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# dic = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#        {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII"}]

# # s = set()

# # for i in dic:
# #     for k, v, in i.items():
# #         s.add(v)
# # print(s)

# s = set()
# for i in dic:
#     for v in i.values():
#         s.add(v)
#         i[v]
# print(s)


# dic = [
#     {"V": "S001"},
#     {"V": "S002"},
#     {"VI": "S001"},
#     {"VI": "S005"},
#     {"VII": " S005 "},
#     {" V ": " S009 "},
#     {" VIII ": " S007 "},
# ]

# s = set()
# for i in dic:
#     for k, v in i.items():
#         s.add(v)

# print(s)

# s = set()
# for i in dic:
#     for v in i.values():
#         s.add(v)
#         i[v]
# print(s)


# Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д.
# Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., а значения - список номеров (следующих в том же порядке, что и во входной строке) с соответствующими кодами.
# Полученный словарь вывести командой:

# print(*sorted(d.items()))

# Sample Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# Sample Output:
# ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])

# number_row = '+71234567890 +71234567854 +61234576890 +52134567890 \
#     +21235777890 +21234567110 +71232267890'
# number_list = list(number_row.split())
# number_dict = dict()

# for i in number_list:
#     if i[:2] in number_dict:
#         number_dict[i[:2]].append(i)
#     else:
#         number_dict[i[:2]] = [i]

# print(*sorted(number_dict.items()))
