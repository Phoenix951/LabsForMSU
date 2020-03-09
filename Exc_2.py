def exercise_one():
    """
    Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
    """
    list_of_numbers = [1, 2, 4, 9, 5, 13, 12, 15, 20]
    list_of_even_numbers = []
    for i in list_of_numbers:
        if int(i) % 2 == 0:
            list_of_even_numbers.append(i)
    print(list_of_even_numbers)


def exercise_two():
    """
    Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
    Если соседних элементов одного знака нет — не выводите ничего.
    Если таких пар соседей несколько — выведите первую пару.
    """
    list_of_numbers = [-1, 1, -3, 5, -2, 6, 9]
    key = 0
    for i in range(len(list_of_numbers) - 1):
        if list_of_numbers[i] > 0 and list_of_numbers[i + 1] > 0 and key == 0:
            print(f"{list_of_numbers[i]} : {list_of_numbers[i + 1]}")
            key += 1
        elif list_of_numbers[i] < 0 and list_of_numbers[i + 1] < 0 and key == 0:
            print(f"{list_of_numbers[i]} : {list_of_numbers[i + 1]}")
            key += 1
        else:
            continue


def exercise_three():
    """
    Дан список чисел. Определите, сколько в нем встречается различных чисел.
    """
    list_of_numbers = [3, 12, 15, 5, 9, 3, 1, 21, 30, 15]
    set_of_numbers = set(list_of_numbers)
    key = 0

    for i in set_of_numbers:
        key += 1
    print(f"Список различных чисел: {set_of_numbers}")
    print(f"Количество различных чисел в списке: {key}")


def exercise_four():
    """
    Во входной строке записана последовательность чисел через пробел.
    Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности
    или NO, если не встречалось.
    """
    list_of_numbers = input("Введите числа через пробел:")
    list_of_numbers = [i for i in list_of_numbers.split(" ")]
    required_list_of_numb = []

    for i in list_of_numbers:
        if i not in required_list_of_numb:
            required_list_of_numb.append(i)
            print(f"Число {i} : NO")
        else:
            print(f"Число {i} : YES")


def exercise_five():
    text = """
    В единственной строке записан текст. 
    Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
    Словом считается последовательность непробельных символов идущих подряд, 
    слова разделены одним или большим числом пробелов или символами конца строки.
    """
    text = [i for i in text.split()]
    dict_text = {}
    for i in text:
        if i not in dict_text.keys():
            dict_text.update({i: 1})
        else:
            dict_text.update({i: dict_text.get(i) + 1})
    print(dict_text)


def exercise_six():
    """
    Дан список стран и городов каждой страны. Затем даны названия городов.
    Для каждого города укажите, в какой стране он находится.
    """
    list_of_countries = ["Америка", "Канада", "Норвегия"]
    list_of_cities = ["Нью-Йорк", "Чикаго", "Вашингтон",
                      "Торонто", "Ванкувер", "Оттава",
                      "Осло", "Ессхейм", "Ставангер"]
    dict_coun_and_city = {}
    res = []
    for i in list_of_countries:
        for j in list_of_cities[:3]:
            res.append(j)
        list_of_cities = list_of_cities[3:]
        dict_coun_and_city.update({i: res})
        res = []
    print(dict_coun_and_city)

    name_city = input("Введите название города: ")

    for key, item in dict_coun_and_city.items():
        for i in item:
            if i == name_city:
                print(f"Страна в которой находиться город {name_city} это {key}")


# exercise_one()
# exercise_two()
# exercise_three()
# exercise_four()
# exercise_five()
# exercise_six()
