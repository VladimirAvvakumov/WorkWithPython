#Пишем функцию которая наполняе список через компрехеншен и заполняет его
#
#
#
#
# def func(n):
#     res = [el for el in range(n)]
#     return res
# print(func(1000))


# def func2(n):
#     for el in range(n):
#         yield el 
# for el in func2(5): # генератор разовая функция. Работает один раз. Если надо ещё пишем новый
#     print(el , end=', ')

#print((al for al in range(5)))


print({el: el for el in range(5)})