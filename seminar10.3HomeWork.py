#  В ячейке ниже представлен код генерирующий DataFrame, 
# которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())


#1 не без помощи зала но вот))
data['isRobot'] = data['whoAmI'] == 'robot'
data['isHuman'] = data['whoAmI'] == 'human'
del data['whoAmI']   # удаляем исходный столбец, так как он нам больше не нужен
print(data.head())

# Генерация данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# Преобразование в one hot
# создаём новый пустой объект DataFrame и кладём в переменную one_hot
one_hot = pd.DataFrame()
# Создаём цикл, который проходит по каждой категории из списка уникальных значений столбца whoAmI data['whoAmI'].unique()
for category in data['whoAmI'].unique():
    one_hot[category] = (data['whoAmI'] == category).astype(int) # добавляем столбец, в котором имя стобца соответсвует категории, значением будет булевый массив, преобразованный в численный

# Печать результата 
print(one_hot.head())