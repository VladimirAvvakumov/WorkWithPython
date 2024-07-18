# Задача №3. Решение в группах 1. Определить какое максимальное и минимальное 
# значение median_house_value 1. Показать максимальное median_house_value, 
# где median_income = 3.1250 1. Узнать какая максимальная population 
# в зоне минимального значения median_house_value

from pandas import read_csv 

file_path = 'california_housing_test.csv'
data = read_csv(file_path)
#1  Определить какое максимальное и минимальное 
# значение median_house_value 1

print(f'Минимальное - {data["median_house_value"].min()},максимальное - {data["median_house_value"].max()}')

#2 Показать максимальное median_house_value, 
# где median_income = 3.1250 1

print(data[data['median_income'] == 3.1250]['median_house_value'].max())


#3 Узнать какая максимальная population 
# в зоне минимального значения median_house_value

print(data[data['median_house_value'] == data['median_house_value'] .min()]['population'].max())



 