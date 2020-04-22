def exercise_one():
    """
    Задание 1.
    Пусть дана строка, состоящая из слов, пробелов и знаков припинания.
    На основании этой строки создайте новую, Содержащую только слова, в которых две последние буквы 'ов'
    :return:
    """
    input_string = input("Введите стрку: ").split(" ")
    string_with_letters = [string for string in input_string if string[-2:] == 'ов']
    new_string = " ".join(string_with_letters)
    print(new_string)


def exercise_two_and_three():
    """
    В данной функции выполняется задание два и три.
    :return:
    """
    # Импортирование сторонних модулей
    from prettytable import PrettyTable

    # Строка для вывода
    my_string = """Ф;И;О;О студенте;
    _Иванов;Иван;Иванович;23 года;Студент 3 курса;
    _Петров;Семен;Игоревич;22 года;Студент 2 курса;
    _Крутиков;Артем;Александрович;24 года;Студент 3 курса;
    _Акибов;Ярослав;Наумович;23 года;Студент 3 курса;
    _Борков;Станислав;Максимовчи;20 года;Студент 1 курса;
    _Романов;Дмитрий;Сергеевич;24 года;Студент 3 курса
    """.split(';\n')

    list_from_my_string = [string.strip().replace("_", "") for string in my_string]
    new_list = [string.split(";") for string in list_from_my_string]
    new_list[0][0:3] = ["".join(new_list[0][0:3])]

    for i in new_list[1:]:
        i[-2], i[-1] = i[-1], i[-2]
        i[0:3] = [" ".join(i[0:3])]
        i[1:3] = [" ".join(i[1:3])]

    # Создание таблицы для первого задания
    header = new_list[0]
    table_for_exc_one = PrettyTable(header)
    table_for_exc_one.align["ФИО"] = "l"
    table_for_exc_one.align["О студенте"] = "l"

    # Добавление элементов в таблицу для первого задания
    for data in new_list[1:]:
        table_for_exc_one.add_row(data)

    # Вывод таблицы для второго задания
    print(table_for_exc_one)

    # Создание таблицы для третьего задания
    table_for_exc_two = PrettyTable(header)
    table_for_exc_two.align["ФИО"] = "l"
    table_for_exc_two.align["О студенте"] = "l"

    # Добавление элементов в таблицу для третьего задания
    for data in new_list[1:]:
        if data[0].startswith("А") or data[0].startswith("Б"):
            table_for_exc_two.add_row(data)

    # Вывод таблицы для третьего задания
    print(table_for_exc_two)


def exercise_four():
    """
    Задание 4.
    Пусть дана строка произвольной длины. Выведите информацию о том,
    сколько в ней символов и сколько слов.
    :return:
    """
    input_string = input("Введите строку: ")
    words = len(input_string.split())
    letters = len("".join(input_string.split()))

    print(f"В строке ({input_string}) присутствует {words} слов и {letters} букв")


# exercise_one()
# exercise_two_and_three()
exercise_four()
