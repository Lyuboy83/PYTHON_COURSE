# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()


# N = "a a a b c a a d c d d f".split()
# count = 0

# for i in range(len(N)):
#     for j in range(i + 1, len(N)):
#         if N[i] == N[j]:
#             count += 1
#             N[j] += '_' + str(count)
#     count = 0

# print(*N)


# Алан

# def task1(input_str):
#     char_count = {}
#     result = []

#     characters = input_str.split()

#     for char in characters:
#         if char in char_count:
#             # char_count[char] += 1
#             print(f"{char}_{char_count[char]}", end=' ')
#         else:
#             # char_count[char] = 0  # a = 0 -> a a = 1
#             print(char, end=' ')
#             # result.append(char)
#         char_count[char] = char_count.get(char, 0) + 1
#     # return ' '.join(result)


# input_str = "a a a b c a a d c d d"  # a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# task1(input_str)


# Задача No27. Решение в группах
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13


# str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".lower()
# result = str.split()
# print(result)
# dict = []
# for i in result:
#     if i not in dict:
#         dict.append(i)
# print(len(dict))


# Алексей

# number_row = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# number_list = list(number_row.lower().replace("."," ").replace("'"," ").split())
# print(number_list)
# print(set(number_list))
# print(len(set(number_list)))
