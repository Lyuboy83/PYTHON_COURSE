# def i(a):
#     return a

# print(i(5))

# # -----------

# i_1 = lambda a: a

# print(i_1(5))

# # -----------

# print((lambda a: a)(5))


# lst = '1 2 4 8 9'.split()

# print(lst)


# lst_1 = list(map(int, lst))

# print(lst_1)


# lst_2 = list(map(lambda a:  a + 2, lst_1))

# print(lst_2)


# lst_3 = list(filter(lambda a:  0, lst_1))

# print(lst_3)

# # ------------

# lst_new = [(6, 8), (3, 7), (3, 2)]

# lst_4 = list(filter(lambda a:  (a[0] + a[1]) < 10, lst_new))

# print(lst_4)

# lst_6 = list(map(int, input()))

# print(lst_6)


# задача №47
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
# Пример ввода и вывода данных представлены на следующем слайде

# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values)) if values == transformed_values:
# print(‘ok’) else:
# print(‘fail’)
# Вывод:
# ok



# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# # values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(lambda a: a, values)) 
# # transformation = list(map(lambda x: values, transformed_values))
# if values == transformed_values:
#     print('ok') 
# else:
#     print('fail')


# Задача No49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), 
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, 
# что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, 
# содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. 
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь.
# Гарантируется, что самая далекая планета ровно одна
# Пример ввода и вывода данных представлены на следующем слайде


# Задача No49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# Сергей
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*max(orbits, key = lambda pair: pair[0] * pair[1] * (pair[0] != pair[1])))

