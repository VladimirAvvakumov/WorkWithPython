"""
Задача №1. Решение в группах
Семинар 1. Ввод-вывод, операторы ветвления
За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.

Input:
n = 700
m = 750
Output:
2
"""
from math import ceil # функция округления до большего числа . работает в том случае если число дробное.  
# модуль math от слова математика. в нём много функций математических. из модуля матс мы импортируем функцию сейл 
n = 700
m = 1400

print(ceil(m / n))  # необходимо вывести перед манипуляциями ceil чтобы число округлилось в большую сторону.
print((m + n - 1) // n)# пишем -1 для получения на выходе 2
print (5 / 2)    # используем деление с остатком 
print(5 // 2) #(5 // -2) Получиться -3 округлиться на автомате.
print(5 % 2) # выходит 1 остаток от деления



