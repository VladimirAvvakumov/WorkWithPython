"""15. Иван Васильевич пришел на рынок и решил купить два арбуза:
 один для себя, а другой для тещи. Понятно, что для себя нужно выбрать
 арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много
 и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
 Помогите ему! Пользователь вводит одно число N – количество арбузов.
 Вторая строка содержит N чисел, записанных на новой строчке каждое.
 Здесь каждое число – это масса соответствующего арбуза
 Input: 5 -> 5 1 6 5 9 Output: 1 9"""

data = [5, 1, 6, 5, 9]
max_l = data[0]
min_l = data[0]
for elem in data:
    if elem > max_l:
        max_l = elem
    if elem < min_l:
        min_l = elem  
print(max_l)
print(min_l)  


def func(data, max_l=data[0], min_l=data[0]):
    if len(data) == 0:
        return max_l, min_l
    if data[0] > max_l:
        max_l = data[0]
    if data[0] < min_l:
        min_l = data[0]      
        
    return func(data[1:],max_l, min_l )

print(func(data))
