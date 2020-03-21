def exercise_one():
    """
    Задание 1
    """
    class MatrixThreeOnThree:
        pass


def exercise_two():
    """
    Написать базовый класс Car, в котором определен метод who, выводящий на экран фразу «Привет я машинка».
    Создать два производных класса DriftCar и Bulldozer, выводящих при вызове метода who фразы «Я супер машинка»
    и «А я бульдозер :(», соответственно.
    Создать объекты всех вышеперечисленных типов и вызвать у них метод who().
    """
    class Car:
        def who(self):
            print("Привет я машинка.")

    class DriftCar(Car):
        def who(self):
            print("Я супер машинка")

    class Bulldozer(Car):
        def who(self):
            print("А я бульдозер :(")

    car = Car()
    car.who()

    drift_car = DriftCar()
    drift_car.who()

    bulldozer = Bulldozer()
    bulldozer.who()


def exercise_three():
    """
    Требуется создать класс студента, хранящий набор оценок.
    У данного класса должна быть возможность:

    •	выводить себя с помощью команды print в формате, указанном выше.
    •	Считать средний балл
    •	Добавлять новые оценки
    •	Конструктор на вход должен принимать имя Студента
    """
    class Student:
        def __init__(self, student, file_name):
            self.student = student
            self.file_name = file_name

        def students_print(self):
            """
            Метод для вывода студента с оценками
            """
            with open(self.file_name) as students_file:
                for student_from_file in students_file:
                    student_name = student_from_file[:student_from_file.index(":")]
                    student_marks = student_from_file[student_from_file.index(":") + 2:]

                    if student_name == self.student:
                        print(f"Студент с именем {student_name} имеет оценки {student_marks}")

        def new_student_mark(self):
            """
            Метод для добавления оценок существующему студенту
            """
            with open(self.file_name, "r") as students_file:
                students_names = students_file.readlines()

            with open(self.file_name, "w") as students_file:
                for names in students_names:
                    if names[:names.index(":")] == self.student:
                        mark = " " + str(input("Введите оценку: "))
                        new_mark = ""

                        while mark != " все":
                            new_mark = new_mark + mark
                            mark = " " + str(input("Введите оценку: "))

                        students_file.write(names.rstrip() + new_mark + "\n")
                    else:
                        students_file.write(names)

        def students_average_mark(self):
            """
            Метод для подсчета среднего балла определенного студента
            """
            average = 0
            count_of_marks = 0
            with open(self.file_name) as students_file:
                for line in students_file:
                    if line[:line.index(':')] == self.student:
                        line = line.split(" ")
                        for numbers in line:
                            if numbers.isdigit():
                                average = average + int(numbers)
                                count_of_marks += 1

                        return average/count_of_marks

    # required_student = input("Введите имя проверяемого студента: ")
    # students = Student("Артем", "pupils.txt")

    # students.students_print()
    # students.students_average_mark()
    # students.new_student_mark()

    class DataBase:
        """
        Требуется написать класс базы данных.
        Конструктор этого класса на вход принимает имя файла, после чего загружает всю информацию из файла,
        создавая набор объектов типа Студент.
        Должна быть предусмотрена возможность добавления, удаления студентов,
        а также возможность вывода всей базы данных в файл.
        Должен быть написан метод, позволяющий находить студента с наивысшим средним баллом.
        """
        STUDENTS = {}

        def __init__(self, file_name):
            self.file_name = file_name

            dict_objects_stud = DataBase.STUDENTS

            with open(file_name) as student_file:
                for names in student_file:
                    name = names[:names.index(":")]
                    dict_objects_stud[name] = type(Student(name, file_name))

        def new_student(self):
            """
            Метод для создания нового студента в базе данных
            """
            with open(self.file_name, "a") as students_file:
                name = "\n" + input("Введите имя нового студента:") + ":"
                students_file.write(name)
                mark = " " + str(input("Введите оценку: "))
                while mark != " все":
                    students_file.write(mark)
                    mark = " " + str(input("Введите оценку: "))

            DataBase.__init__(self, self.file_name)

        def delete_student(self, del_stud_name):
            """
            Метод для удаления требуемого студента из базы
            """
            dict_objects_stud = DataBase.STUDENTS

            del dict_objects_stud[del_stud_name]

            with open(self.file_name, "r") as students_delete:
                student_names = students_delete.readlines()
            with open(self.file_name, "w") as students_delete:
                for names in student_names:
                    if names[:names.index(":")] != del_stud_name:
                        students_delete.write(names)

            DataBase.__init__(self, self.file_name)

        def best_student(self):
            """
            Метод для вывода лучшего студента на основе среднего балла
            """
            dict_objects_stud = DataBase.STUDENTS

            best_student_name = ""
            best_student_mark = 0

            for marks in dict_objects_stud.keys():
                student = dict_objects_stud[marks](marks, self.file_name)
                student_mark = student.students_average_mark()
                if student_mark >= best_student_mark:
                    best_student_mark = student_mark
                    best_student_name = marks

            print(f"Студент с именем {best_student_name} имеет наивысший балл равный {best_student_mark}")

    data_base = DataBase("pupils.txt")

    # data_base.new_student()
    data_base.delete_student("Qwert")
    data_base.best_student()


exercise_three()
# exercise_two()
