def exercise_one(search_number):
    """
    В упорядоченном по возрастанию массиве целых чисел найти определенный элемент (указать его индекс)
    или сообщить, что такого элемента нет.
    Задание 3. Страница 63.
    :param search_number: искомое число
    :return: индекс искомого числа
    """
    list_of_numbers = [5, 1, 12, 15, 2, 9, 21, 45, 33, 30]
    list_of_numbers.sort()

    print(f"Массив чисел: {list_of_numbers}")

    for i in range(len(list_of_numbers)):
        if search_number == list_of_numbers[i]:
            print(f"Индекс числа {search_number} равен {i}")


exercise_one(15)