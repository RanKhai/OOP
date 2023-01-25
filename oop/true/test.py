from .Bachelor import Bachelor
from .Aspirant import Aspirant


def print_students(*students):
    for student in students:
        print(student.name, student.group, student.average_mark, student.get_grant())


def test():
    student_bachelor = Bachelor('Nikolay', '1011', 4)
    student_aspirant = Aspirant('Misha', '12312', 3.21)
    print_students(student_bachelor, student_aspirant)
    student_aspirant.update_average_mark(5)
    student_bachelor.update_average_mark(4.48)
    print_students(student_bachelor, student_aspirant)


if __name__ == '__main__':
    test()
