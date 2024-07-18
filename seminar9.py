# Задача №1. Общее обсуждение 1. Прочесть с помощью pandas файл california_housing_test.csv,
# который находится в папке sample_data 
# 2. Посмотреть сколько в нем строк и столбцов 
# 3. Определить какой тип данных имеют столбцы

from pandas import read_csv 

file_path = 'california_housing_test.csv' # файл являеться относительным ?
data = read_csv(file_path)
print(type(data))

print(data.shape)# функция шейп выводит на экран количество строк и столбцов

print(data.dtypes)# функция узнает какие есть типы данных

print(data.info())# метод(без скобок не работает) инфо показывает  

print(data.describe())# детальная иформация о нашем датафрейме

