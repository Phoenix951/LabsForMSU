# Файл задач повышенно сложности
# Запуск производить через файл Menu.py


def exercise_one(count_of_numbers):
    """
    1. Крайние элементы
    :param count_of_numbers: количество найденных веток
    :return: 3 самых коротких и 3 самых длинных ветки
    """
    all_length = ""
    count = 0

    while count < count_of_numbers:
        branch = input("Введите длину ветки: ")
        all_length = all_length + " " + branch
        count += 1

    all_length = all_length.rstrip().lstrip()
    length_of_branches = all_length.split(" ")

    length_of_branches.sort()
    print(f"Длины всех найденных веток: {length_of_branches}")
    length_of_branches = length_of_branches[:3] + length_of_branches[len(length_of_branches) - 3:]
    print(f"Длины 3 самых коротких и 3 самых длинных веток: {length_of_branches}")


def exercise_two(required_string, required_letter):
    """
    2. Сколько символов
    :param required_string: нужная для проверки строка
    :param required_letter: символ, по которому проводиться поиск
    :return: количество вхождение нужной буквы в строку
    """
    count = 0
    for letter in required_string:
        if letter == required_letter:
            count += 1
    print(f"Количество вхождений буквы {required_letter} в строку {required_string} равно {count}")


def exercise_three(required_numbers_string):
    """
    3. Наибольший остаток
    :param required_numbers_string: строка с нужными числами написанными через пробел
    :return: Число дающее максимальный остаток при делении на 2015
    """
    required_numbers_string = str(required_numbers_string).split(" ")
    required_number = 0
    for number in required_numbers_string:
        if int(number) / 2015 > required_number / 2015:
            required_number = int(number)
    print(f"Число у которого максимальный остаток при делении на 2015, это {required_number}")


def exercise_four(massive_of_numbers):
    """
    4. Суммарная разность
    :param massive_of_numbers: необходимый для вычисления суммы массив чисел
    :return: сумму попарных разностей соседних элементов массива
    """
    difference_btw_numb = []

    for index in range(len(massive_of_numbers) - 1):
        difference_btw_numb.append(int(massive_of_numbers[index + 1]) - int(massive_of_numbers[index]))

    sum_of_numbers = sum(difference_btw_numb)
    print(f"Сумма попарных разностей чисел массива равна {sum_of_numbers}")


def exercise_five(massive_from_three):
    """
    5. Большее произведение
    :param massive_from_three: массив из трех чисел
    :return: наибольшее из указанных произведений
    """
    max_btw_numb = []

    for index in range(len(massive_from_three) - 1):
        max_btw_numb.append(int(massive_from_three[index]) * int(massive_from_three[index + 1]))
    max_number = max(max_btw_numb)

    print(f"Максимум из произведений данных чисел это {max_number}")


def exercise_six(massive_from_three):
    """
    6. Наибольший хвост
    :param massive_from_three: массив из трех чисел
    :return: единственное число, имеющее наибольшее двузначное число в разряде десятков и единиц
    """
    max_number = 0
    max_end_number = 0

    for number in massive_from_three:
        if number % 100 > max_end_number:
            max_end_number = number % 100
            max_number = number

    print(f"Число, имеющее наибольшее двузначное число в разряде десятков и единиц, является {max_number}")


def exercise_seven():
    pass


def exercise_eight(size_of_planets):
    """
    8. Космическая стратегия
    :param size_of_planets: массив состоящий из численности населения всех планет
    :return: в зависимости от массива может возвращать:
    - численность населения, наиболее часто встречающуюся в массиве
    - если таких численностей несколько, наименьшую
    - если нет повторений, выводит сообщение об различной численности населения
    """
    count_of_planets = 0
    planet_that_browsed = []
    dict_of_count = {}

    for planet in size_of_planets:
        if planet not in planet_that_browsed:
            planet_that_browsed.append(planet)

    for planet in planet_that_browsed:
        count = list(size_of_planets).count(planet)
        update_of_planets_count = {planet: count}
        dict_of_count.update(update_of_planets_count)

    for count in dict_of_count.values():
        if count > 1:
            count_of_planets += 1

    if count_of_planets == 0:
        print("Численность населения на планетах различная.")

    elif count_of_planets == 1:
        for key, item in dict_of_count.items():
            if item >= 2:
                print(f"Наиболее часто встречающееся численность населения равна {key}")

    elif count_of_planets >= 2:
        min_count = []
        for key, item in dict_of_count.items():
            if item >= 2:
                min_count.append(key)
        print(f"Наименьшое количество населения равно {min(min_count)}")


def exercise_nine(massive_of_numbers):
    """
    9. Вариация массива
    :param massive_of_numbers: массив из целых чисел
    :return: сумма разностей элементов массива
    """
    massive_of_numbers.sort()

    difference_btw_numb = []

    for number in range(len(massive_of_numbers) - 1):
        difference_btw_numb.append(massive_of_numbers[number + 1] - massive_of_numbers[number])

    result_of_dif = sum(difference_btw_numb)

    print(f"Результат сложения разностей чисел массива равен {result_of_dif}")


def exercise_ten(required_string):
    """
    10. Учим слова
    :param required_string: введеная строка
    :return: количество слов, которые начинаются с R
    """
    count_of_entry = 0

    required_string = required_string.upper().split(" ")

    for string in required_string:
        if string.startswith("R"):
            count_of_entry += 1

    print(f"Количество слов начинающихся с буквы R в строке равно {count_of_entry}")
