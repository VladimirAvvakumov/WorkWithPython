# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго 
# Ввод: 7 3 1 3 4 2 4 12   6  4 15 43 1 15 1 
# Вывод: 3 3 2 12 массива 
# (каждое число вводится с новой строки)

num_1 = [3, 1, 3, 4, 2, 4, 12]
num_2 =[4, 15, 43, 1, 15, 1]
num_3 = []
#num_4 = list(map(int, input('введите числа через пробел ...').split())) #функция map вернет обьект в типе данных map

# for el in num_1: # циклом фор проходим по каждому элементу массива num_1
#      if el not in num_2: # условие если переменной el нет в массиве num_2
#         num_3.append(el) # то с помощью функции append вносим их в список num_3
# print('Решение через традиционный итеиратор с функцией append')
# print(num_3)  

def func(num_1, num_2, num_3 = []):
    if len(num_1) == 0:
        return num_3
    if num_1[0] not in num_2:
        num_3.append(num_1[0])
    return func(num_1[1:], num_2 , num_3) 
print(func(num_1, num_2, num_3))

# num_5 = [elem for elem in num_1 if elem not in num_2]
# print('\nРешение с применение list comprehensions')
# print(num_5)



# res = filter(lambda elem: elem not in num_2, num_1)
# print('\nРешение через использование функций filter , lambda')
# print(', '.join(str(elem) for elem in res))




