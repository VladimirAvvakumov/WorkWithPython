#У вас есть код, который вы не можете менять 
#(так часто бывает, когда код в глубине программы используется множество раз
# и вы не хотите ничего сломать): 
#transformation = <???> values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] 
# или любой другой список transormed_values = list(map(transformation, values)) 
# Единственный способ вашего взаимодействия с этим кодом - 
# посредством задания функции transformation. Однако вы поняли, что для вашей 
# текущей задачи вам не нужно никак преобразовывать список значений, 
# а нужно получить его как есть. Напишите такое лямбда-выражение transformation, 
# чтобы transformed_values получился копией values.

#Ввод: 
# values = [1, 23, 42, 'asdfg'] 
# transformed_values = list(map(trasformation, values)) 
# if values == transformed_values:    
#     print('ok') 
# else:    
#     print('fail') 
#Вывод: ok

# def func(a, b):  # именная фунуция
#     return a**b
# print(func(1 , 2))

# func = lambda a, b : a ** b # переменная ссылаеться на функцию лямбда
# print(func(1, 2)) # для вывода на экран результата надо добавить значение переменных если их нет выше.


# print((lambda a, b: a ** b)(1, 2))# в одну строку
transformation = lambda a: a # ссылаеться на обьект с лямбда функцией
values = [1, 23, 42, "asdfg"]
transformed_values = list(map(transformation, values))# функция map применяет какую то функцию к каждому элементу списка
if values == transformed_values:
    print("ok")
else:
    print("fail")





