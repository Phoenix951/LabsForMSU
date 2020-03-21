
"""
Задача 1.
Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е. соединение, строк.
В остальных случаях введенные числа суммируются.
"""
string_one = input("Введите первую строку: ")
string_two = input("Введите вторую строку: ")

if string_one.isdigit() is False or string_two.isdigit() is False:
    result = string_one + string_two
else:
    result = int(string_one) + int(string_two)

print(result)

