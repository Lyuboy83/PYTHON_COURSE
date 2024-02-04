# w - запись
# r - чтение
# a - добавить
# a = ["q\n","r\n","e\n"]
# with open("input.txt","w") as file:
#     file.write("strq\n")
#     file.writelines(a)
# with open("input.txt","r") as file:
# print(file.read())
# file.seek(0)
# print(file.readlines())
# for i in range(4):
#     print(file.readline(i))#
# a = list(map(lambda x: x.strip(),file.readlines()))


# with open("input.txt", "a") as file:
#     file.write("qw")

# from database import *
# from view import *

# def main():
#     while True:
#         num = input_num()
#         if num == 1:
#             name = input_name()
#             write_name(name)
#             print("Успешно записано\n")


# main()

# 20:31
# def input_num():
#     ask = int(input("Выбери действие:\n1 - Записать нового пользователя\n2-Изменить..."))
#     return ask

# def input_name():
#     pass


# id,ФИО,дата рождения
# 21,Максим Иванов,29.05.1999
# 1)Ввод нового пользователя
# 2)Поиск по определенной характеристике -> ввод хар-стики, предлагаем на выбор строчки подходящие, полтзователь 
# выбирает и мы изменяем

# a = ["10,Иван,15","3,Алеша,10",]
# a.sort(key = lambda x: int(x.split(",")[2]))
#print(a)
# a = [(6,5),(8,2),(3,7),(1,4),]
# print(max(a,key=lambda x: x[1]))
# print(a)


# Предыдущее ДЗ

#Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# stroka1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# lst = []
# for phrase in stroka1.split():
#     count_vow = 0
#     for letter in phrase:
#         if letter in vowels:
#             count_vow += 1
#     lst.append(count_vow)
#
# if lst.count(lst[0]) == len(lst):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


#  2-е.

# def print_operation_table(operation, num_rows = 9, num_columns = 9):
#     for row in range(1,num_rows+1):
#         for col in range(1,num_columns+1):
#             print(operation(row,col), end = '\t')
#         print()

# print_operation_table(lambda x, y: x * y)