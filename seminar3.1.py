# Решение в группах
#Дана последовательность из N целых чисел и число
#K. Необходимо сдвинуть всю последовательность
#(сдвиг - циклический) на K элементов вправо, K –
#положительное число.
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]

my_list = [1, 2, 3, 4, 5]
k = 3 

new_list = my_list[k:] + my_list[:k] # складываем часть массива от третьего элемента
print(new_list) # плюс чать после третьего с конца "смотри лекция номер 2"

for _ in range(k - 1): # если переменная не нужна то ставим ниж подчеркивание шаг с конца(range)
    last = my_list.pop() # функция pop удаляет  
    my_list.insert(0 , last) # вставка в начало списка метод insert (обозначено что вставка идет в начало списка и)
print(my_list) # вставляем числа сохраненные в переменной last