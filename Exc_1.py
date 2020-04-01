def exercise_one():
    """
    Дан файл с расписанием занятий на неделю.
    Помимо названия предмета в нем также указано лекция это, или практическое занятие, или лабораторная работа.
    В одной строке может быть указаны только один предмет с информацией о нем.
    Посчитать, сколько за неделю проходит практических занятий, лекций и лабораторных работ.
    """
    labs = 0
    lectures = 0
    practice = 0

    read_file = open("days.txt")

    for day in read_file:
        day = day.rstrip("\n")
        if day.find("лабораторная") > 0:
            labs += 1
        elif day.find("лекция") > 0:
            lectures += 1
        elif day.find("практика") > 0:
            practice += 1

    read_file.close()
    print("Лабораторные: ", labs)
    print("Лекции: ", lectures)
    print("Практические занятия: ", practice)


def exercise_two():
    """
    Пользователь вводит числа в строку через пробел. Когда он нажимает Enter, на экран выводится сумма.
    Пользователь может снова вводить числа. Их сумма будет добавляться к уже посчитанной, и итог выводиться на экран.
    Когда вместо чисел вводится специальный символ, программа завершается.
    """
    numbers_string = input("Введите числа: ").split(" ")

    def sum_of_numbers(numbers_in_string):
        sum_of_req_numbers = 0
        print(numbers_in_string)
        for i in numbers_in_string:
            if i.isdigit():
                sum_of_req_numbers = sum_of_req_numbers + int(i)
        return sum_of_req_numbers

    numbers = sum_of_numbers(numbers_string)

    print("Сумма чисел: ", numbers)
    another_number = input("Введите число: ")
    while another_number.lower() != "все":
        numbers = numbers + sum_of_numbers(another_number)
        print("Сумма чисел: ", numbers)
        another_number = input("Введите число: ")
    print("Конечная сумма: ", numbers)


def exercise_three():
    """
    В заданной строке найти самое короткое слово.
    """
    input_string = "name is Artem"
    required_string = input_string.split(' ')

    string_with_min_letters = required_string[0]

    for index in range(1, len(required_string) - 1):
        if len(required_string[index]) < len(string_with_min_letters):
            string_with_min_letters = required_string[index]

    max_number = len(string_with_min_letters)
    print(f"Строка с минимальным числом букв это - {string_with_min_letters} и она имеет {max_number} буквы/букв")


def exercise_four():
    """
    Из списка чисел удалить элементы, значения которых больше 35 и меньше 65.
    При этом удаляемые числа сохранить в другом списке.
    """
    mas_a = [80, 35, 30, 98, 35, 4, 94, 51, 22, 22, 52, 97, 67, 90, 9, 1, 87, 78, 100, 29]
    mas_b = [i for i in mas_a if 35 < i < 65]

    print("Первоначальный массив:\n", mas_a)
    i = 0
    while i < len(mas_a):
        if 35 < mas_a[i] < 65:
            del mas_a[i]
        i += 1

    print("Массив А после удаления:\n", mas_a)
    print("Массив В после удаления из А:\n", mas_b)


def exercise_five():
    """
    Определить, сколько в числе четных цифр, а сколько нечетных. Число вводится с клавиатуры.
    """
    numbers_even_count = 0
    numbers_odd_count = 0
    number = input("Введите число для проверки: ")

    while number.isalpha():
        print("Введено некорректное значение.")
        number = input("Введите число для проверки: ")
    for i in number:
        if int(i) % 2 == 0:
            numbers_even_count += 1
        elif int(i) % 2 != 0:
            numbers_odd_count += 1
    print(f"Число четных цифр: {numbers_even_count}")
    print(f"Число нечетных цифр: {numbers_odd_count}")


def exercise_six():
    """
    Определить, принадлежит ли точка с координатами (x; y) кругу радиуса R с центром в начале координат.
    """
    start_x = 0
    start_y = 0

    radius = int(input("Введите радиус круга: "))
    x_coord = int(input("Введите координату х: "))
    y_coord = int(input("Введите координату y: "))

    coordinate = pow((x_coord - start_x), 2) + pow((y_coord - start_y), 2)

    if coordinate <= pow(radius, 2):
        print("Точка принадлежит окружности.")
    else:
        print("Точка не принадлежит окружности.")


def exercise_seven():
    """
    Вводятся два числа в двоичной системе счисления.
    Требуется выполнить над ними побитовые операции И, ИЛИ и исключающее ИЛИ.
    Вывести результат операций в двоичном представлении.
    """
    number_one = int(input("Введите первое число: "), 2)
    number_two = int(input("Введите второе число: "), 2)

    print(bin(number_one))
    print(bin(number_two))
    result_or = bin(number_one | number_two)
    result_not_or = bin(number_one ^ number_two)
    result_and = bin(number_one & number_two)

    print(f"Результат побитового OR: {result_or}")
    print(f"Результат побитового AND: {result_and}")
    print(f"Результат побитового XOR: {result_not_or}")


# exercise_one()
# exercise_two()
# exercise_three()
# exercise_four()
# exercise_five()
# exercise_six()
# exercise_seven()
