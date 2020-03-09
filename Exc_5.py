def exercise_one(input_string):
    """
    Определить, является ли введенное слово идентификатором, т.е. начинается ли оно с английской буквы в любом регистре
    или знака подчеркивания и не содержит других символов,
    кроме букв английского алфавита (в любом регистре), цифр и знака подчеркивания.
    """
    import string
    list_of_letters = [i for i in string.ascii_letters]
    list_of_letters.append("_")
    list_of_letters.append("_")

    required_string = str(input_string)

    for letter in list_of_letters:
        if required_string.startswith(letter):
            print(f"Слово {required_string} явлется идентификатором")
            break
    else:
        print(f"Слово {required_string} не является идентификатором")


def exercise_two(new_string):
    """
    Вводится строка. Удалить из нее все пробелы.
    После этого определить, является ли она палиндромом (перевертышем), т.е.
    одинаково пишется как с начала, так и с конца.
    """
    required_string = str(new_string)
    required_string = required_string.replace(" ", "").lower()

    print(required_string)
    reversed_string = required_string[::-1]
    print(reversed_string)

    if required_string == reversed_string:
        print(f"Строка {new_string} является полиндромом")
    else:
        print(f"Строка {new_string} не является полиндромом")


def exercise_three(new_string):
    """
    Вводится строка, содержащая буквы, целые неотрицательные числа и иные символы.
    Требуется все числа, которые встречаются в строке, поместить в отдельный целочисленный массив.
    Например, если дана строка "data 48 call 9 read13 blank0a", то в массиве должны оказаться числа 48, 9, 13 и 0.
    """
    required_string = new_string.split()
    list_of_numbers = []

    print(required_string)
    for number in required_string:
        if len(number) == 1:
            if number.isdigit():
                list_of_numbers.append(number)
        string = ""
        for i in range(len(number) - 1):
            if number[i - 1].isalpha() and number[i].isdigit():
                string = number[i]
            elif number[i].isdigit() or number[i + 1].isdigit():
                string = string + number[i]
            if number[i + 1] == number[-1] and number[i + 1].isdigit():
                string = string + number[i + 1]
        if string == "":
            continue
        list_of_numbers.append(string)

    print(list_of_numbers)


def exercise_four(new_string):
    """
    Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
    Например, если было введено "abc cde def", то должно быть выведено "abcdef".
    """
    new_string = str(new_string)
    required_string = ""
    print(f"Первоначальная строка: {new_string}")
    new_string = new_string.replace(" ", "")

    for letter in new_string:
        if letter not in required_string:
            required_string = required_string + letter

    print(f"Строка без повторяющихся символов: {required_string}")


def exercise_five(new_string, string_for_replace, replaced_string):
    """
    Найти в строке указанную подстроку и заменить ее на новую.
    Строку, ее подстроку для замены и новую подстроку вводит пользователь.
    """
    result_string = str(new_string).replace(string_for_replace, replaced_string)

    print(f"Строка с заменой: {result_string}")


def exercise_six(*args):
    """
    Вводятся строки. Определить самую длинную строку и вывести ее номер на экран.
    Если самых длинных строк несколько, то вывести номера всех таких строк.
    """
    list_of_strings = args
    dict_of_strings = {}
    max_item = len(list_of_strings[0])

    for i in range(0, len(list_of_strings)):
        if len(list_of_strings[i]) > max_item:
            max_item = len(list_of_strings[i])
            dict_of_strings.update({f"Максимальной строкой является: '{list_of_strings[i]}' и ее индекс:": i})
    if dict_of_strings == {}:
        for i in range(0, len(list_of_strings)):
            if len(list_of_strings[i]) == max_item:
                dict_of_strings.update({f"Максимальной строкой является: '{list_of_strings[i]}' и ее индекс:": i})

    print(dict_of_strings)


def exercise_seven(new_string):
    """
    Вводится строка слов, разделенных пробелами. Найти самое длинное слово и вывести его на экран.
    Случай, когда самых длинных слов может быть несколько, не обрабатывать.
    """
    list_of_strings = str(new_string).split()
    dict_of_strings = {}
    max_item = len(list_of_strings[0])

    for i in range(1, len(list_of_strings)):
        if len(list_of_strings[i]) > max_item:
            max_item = len(list_of_strings[i])
            dict_of_strings.update({f"Максимальной строкой является: '{list_of_strings[i]}' и ее индекс:": i})
        if len(list_of_strings[i]) == max_item:
            dict_of_strings.update({f"Максимальной строкой является: '{list_of_strings[i]}' и ее индекс:": i})
    if dict_of_strings == {} or len(list_of_strings[0]) == max_item:
        dict_of_strings.update({f"Максимальной строкой является: '{list_of_strings[0]}' и ее индекс:": 0})

    if len(dict_of_strings.keys()) > 1:
        print("Случай, когда самых длинных слов несколько.")
    else:
        print(dict_of_strings)


def exercise_eight(new_string):
    """
    Вводится ненормированная строка, у которой могут быть пробелы в начале,
    в конце и между словами более одного пробела.
    Привести ее к нормированному виду, т.е. удалить все пробелы в начале и конце,
    а между словами оставить только один пробел.
    """
    list_string = str(new_string).split()
    required_string = ""

    for i in list_string:
        required_string = required_string + " " + i
    required_string = required_string.lstrip()

    print(f"Строка: '{required_string}'")


def exercise_nine(new_string):
    """
    Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
    Учитывать только английские буквы.
    """
    lower_letters = 0
    upper_letters = 0

    new_string = str(new_string)

    for i in new_string:
        if i.islower():
            lower_letters += 1
        elif i.isupper():
            upper_letters += 1

    print(f"Количество: \nСтрочных букв = {lower_letters} \nПроисных букв = {upper_letters}")


def exercise_ten(new_string):
    """
    Вводится строка, состоящая из слов, разделенных пробелами. Требуется посчитать количество слов в ней.
    """
    list_of_strings = str(new_string).split()
    count_of_strings = 0

    for i in list_of_strings:
        count_of_strings += 1

    print(f"Количество слов в строке '{new_string}' равно {count_of_strings}")


# exercise_one("123")
# exercise_two("Тонет енот")
# exercise_three("data 48 call 9  read13a blank0a")
# exercise_four("abc cde def")
# exercise_five("Hello", "el", "123")
# exercise_six("Определитaa", "самую", "длинную", "строку", "Определитab")
# exercise_seven("Вводитсяsssssss строка слов, разделенныхsssss пробеламиaaaaaaa")
# exercise_eight("    ABdas        sfisf    foafg  ")
# exercise_nine("CorREct AnswerS")
# exercise_ten("Требуется посчитать количество слов в ней")