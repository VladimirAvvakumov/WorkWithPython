# Дан массив, состоящий из целых чисел. Напишите программу, 
# которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве  
# Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел. Ввод: 
# Ввод:  1 2 3 4 5   1 5 1 5 1 Вывод: 
# Вывод: 0             2 (каждое число вводится с новой строки)
lst = [1, 2, 3, 4, 5]
lst1 = [1, 5, 1, 5, 1]
count1 = 0
for i in range(1, len(lst1) - 1):# проходим по массиву начиная с второго элемента и последний элемент отсекаем
    if lst1[i] > lst1[i-1] and lst1[i] > lst1[i + 1]:# если текущий элемент больше чем предидущий и текущий больше чем следующий
        count1 += 1
print(count1)        