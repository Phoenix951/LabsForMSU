# Файл для выполнения заданий повышенной сложности (файл Exc_8.py)
from Exc_8 import exercise_one, exercise_two, exercise_three, exercise_four, exercise_five, \
    exercise_six, exercise_seven, exercise_eight, exercise_nine, exercise_ten


def tasks_execution(number_of_task):
    if number_of_task == 1:
        """
            1. Крайние элементы в заданиях повышенной сложности
            :param count_of_numbers: количество найденных веток
            :return: 3 самых коротких и 3 самых длинных ветки
        """
        number_for_exc_one = int(input("Введите количество веток: "))
        while 1000 < number_for_exc_one or number_for_exc_one < 2:
            print("Не верное количество веток")
            number_for_exc_one = int(input("Введите количество веток: "))

        exercise_one(number_for_exc_one)

    elif number_of_task == 2:
        """
            2. Сколько символов
            :param required_string: нужная для проверки строка
            :param required_letter: символ, по которому проводиться поиск
            :return: количество вхождение нужной буквы в строку
        """
        required_string = input("Введите строку: ")
        while len(required_string) > 255:
            print("Длина строки превышает 255 символов.")
            required_string = input("Введите строку: ")
        required_letter = input("Введите букву, количество вхождений которой трубуется посчитать: ")
        exercise_two(required_string, required_letter)

    elif number_of_task == 3:
        """
            3. Наибольший остаток
            :param required_numbers_string: строка с нужными числами написанными через пробел
            :return: Число дающее максимальный остаток при делении на 2015
        """
        required_number_string = []
        count_of_numbers = int(input("Введите количество чисел в массиве: "))

        while 1000 < count_of_numbers or count_of_numbers < 2:
            print("Не верное количество чисел")
            count_of_numbers = int(input("Введите количество чисел в массиве: "))

        for numbers in range(count_of_numbers):
            number_string = input("Введите нужное число: ").split(" ")[0]
            while int(number_string) > 10**8:
                print("Число больше 10 в 8 степени.")
                number_string = input("Введите нужное число: ").split(" ")[0]

            required_number_string.append(number_string)

        exercise_three(required_number_string)

    elif number_of_task == 4:
        required_number_string = []
        count_of_numbers = int(input("Введите количество чисел в массиве: "))

        while 1000 < count_of_numbers or count_of_numbers < 2:
            print("Не верное количество чисел")
            count_of_numbers = int(input("Введите количество чисел в массиве: "))

        for numbers in range(count_of_numbers):
            number_string = input("Введите нужное число: ").split(" ")[0]
            while int(number_string) > 10 ** 6:
                print("Число больше 10 в 8 степени.")
                number_string = input("Введите нужное число: ").split(" ")[0]

            required_number_string.append(number_string)

        print(required_number_string)
        exercise_four(required_number_string)

    elif number_of_task == 5:
        """
            5. Большее произведение
            :param massive_from_three: массив из трех чисел
            :return: наибольшее из указанных произведений
        """
        print("Введите три числа. (Если будет введено больше, будут взяты первые 3)")

        massive_from_numb = input("Введите необходимые числа через пробел: ").rstrip().lstrip().split(" ")[:3]

        for number in massive_from_numb:
            if abs(int(number)) > 30000:
                print("Введены не верные числа. Могут быть неверные результаты. Рекомендуется повторить попытку.")

        exercise_five(massive_from_numb)

    elif number_of_task == 6:
        """
            6. Наибольший хвост
            :param massive_from_three: массив из трех чисел
            :return: единственное число, имеющее наибольшее двузначное число в разряде десятков и единиц
        """
        required_string = input("Введите числа через пробел: ").lstrip().rstrip().split(" ")
        required_string = required_string[:3]

        required_string = list(map(int, required_string))

        for number in required_string:
            if 10 ** 6 < number or number < 10:
                print("Введены не верные числа. Могут быть неверные результаты. Рекомендуется повторить попытку.")

        exercise_six(required_string)

    elif number_of_task == 7:
        pass
    elif number_of_task == 8:
        """
            8. Космическая стратегия
            :param size_of_planets: массив состоящий из численности населения всех планет
            :return: в зависимости от массива может возвращать:
            - численность населения, наиболее часто встречающуюся в массиве
            - если таких численностей несколько, наименьшую
            - если нет повторений, выводит сообщение об различной численности населения 
        """
        size_of_planats = []

        number_of_planets = int(input("Введите количество планет: "))

        while 10 ** 5 < number_of_task or number_of_task == 0:
            print("Введено неверное количество планет. Повторите попытку.")
            number_of_planets = int(input("Введите количество планет: "))

        for pl_number in range(number_of_planets):
            planet_size = int(input("Введите численность населения планеты: "))
            while planet_size > 10 ** 9:
                print("Введено неверное количество населения. Повторите попытку.")
                planet_size = int(input("Введите численность населения планеты: "))
            size_of_planats.append(planet_size)

        exercise_eight(size_of_planats)

    elif number_of_task == 9:
        """
            9. Вариация массива
            :param massive_of_numbers: массив из целых чисел
            :return: сумма разностей элементов массива
        """
        massive_of_numbers = []

        count_of_numbers = int(input("Введите количество элементов в массиве: "))
        while 1000 < count_of_numbers or count_of_numbers < 2:
            print("Введено неверное число элементов в массиве. Повторите попытку.")
            count_of_numbers = int(input("Введите количество элементов в массиве: "))

        for count in range(count_of_numbers):
            number = int(input("Введите число: "))
            while 10 ** 6 < number:
                print("Введено неверное число. Повторите попытку.")
                number = int(input("Введите число: "))
            massive_of_numbers.append(number)

        exercise_nine(massive_of_numbers)

    elif number_of_task == 10:
        """
            10. Учим слова
            :param required_string: введеная строка
            :return: количество слов, которые начинаются с R
        """
        required_string = input("Введите строку: ")

        while len(required_string) > 255:
            print("Введенная строка имеет более 255 символов. Повторите попытку.")
            required_string = input("Введите строку: ")

        exercise_ten(required_string)

    elif number_of_task > 10:
        print("Ошибка. Неверное значение. Отключение программы.")

    elif number_of_task == 0:
        print("Выход из программы. Удачного дня.")


task = int(input("Введите номер задания: "))
tasks_execution(task)
