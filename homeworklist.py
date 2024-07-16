def find_indices_vertical(list_1, min_number, max_number):
    # Перебираем элементы списка и их индексы
    for index, value in enumerate(list_1):
        # Проверяем, удовлетворяет ли элемент условиям диапазона
        if min_number <= value <= max_number:
            # Выводим индекс элемента
            print(index)

# Данные для примера
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

# Вызов функции
find_indices_vertical(list_1, min_number, max_number)