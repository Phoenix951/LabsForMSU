def good():
    """
    Определите функцию good, которая возвращает список ['Harry', 'Ron', 'Hermione'].
    """
    return ["Harry", "Ron", "Hermione"]


def square(number_of_length):
    """
    Написать функцию square, принимающую 1 аргумент — сторону квадрата,
    и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
    """
    square_perimeter = number_of_length * 4
    square_area = number_of_length ** number_of_length
    diagonal_of_square = number_of_length * (2 ** 0.5)

    res = (square_perimeter, square_area, diagonal_of_square)

    return res


def is_year_leap(leap_year):
    """
    Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе
    """
    if leap_year % 4 != 0 or (leap_year % 100 == 0 and leap_year % 400 != 0):
        return False
    else:
        return True


def is_prime(number):
    """
    Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
    и возвращающую True, если оно простое, и False - иначе.
    """
    list_of_numbers = [2]
    for i in range(3, 1001, 2):
        if i > 10 and i % 10 == 5:
            continue
        for j in list_of_numbers:
            if j * j - 1 > i:
                list_of_numbers.append(i)
                break
            if i % j == 0:
                break
        else:
            list_of_numbers.append(i)
    if number in list_of_numbers:
        return True
    else:
        return False


number_for_all = int(input("Введите требуемое число для задания"))

# print(good())
# print(square(number_for_all))
# print(is_year_leap(number_for_all))
# print(is_prime(number_for_all))
