# Общее обсуждение 5 минут Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке. Примечание.
# В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input:    2 -> 3 4 
# Output: 4 3

num = '3 4'


def func1(num):
    new_data = ""
    for i in reversed(num):
        new_data += i
    return new_data    
print(func1(num))

def func2(num, new_data = ""): 
    if len(num) == 0:
        return new_data
    return func2(num[:-1], new_data + num[-1])
print(func2(num))