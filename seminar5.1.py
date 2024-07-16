# Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот:
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1


List_1 = [1, 3, 3, 3, 4]
min_grade = min(List_1) 
max_grade = max(List_1)
new_list = []
for grade in List_1:
    if grade == max_grade:
        new_list.append(min_grade)
    else:
        new_list.append(grade)
print(new_list)             

print([min_grade if grade == max_grade else grade for grade in List_1 ])

# отличный способ написания рекурсии(1. создаем функцию def(передаем данные которые есть до цикла))
#2.следом вызываем рекурсию(с необходимым шагом) 3.пишем базовый случай между объявлением функции и ее вызовом
def func(List_1, new_list = [], min_grade = min(List_1), max_grade = max(List_1) ):
    if len(List_1) == 0:
        return new_list
    if List_1[0] == max_grade:
        new_list.append(min_grade)
    else:
        new_list.append(List_1[0])
    return func(List_1[1:], new_list )
print(func(List_1))
