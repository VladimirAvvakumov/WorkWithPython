#Решение в группах
#Напишите программу для печати всех уникальных
#значений в словаре.
#Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
#":" S007 "}]
#Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
#"""
my_list = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"},
{"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

# традиционный итератор с методом add

unique_values = set() # создали пустое множество
for item in my_list:# циклом по каждому очередному словарю из списка
    for value in item.values():# values-массив значений нашего словаря
        unique_values.add(value)# сохраняем значения без ключей . из всех словарей.
print(unique_values)       # 
#set_ coprehensions способ в одну строку
print(set(value for item in my_list for value in item.values()))
