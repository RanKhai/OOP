from .Bachelor import create_bachelor
from .Aspirant import create_aspirant
from .Student import update_average_mark, get_grant


def print_students(*students):
    for student in students:
        print(student['student'], get_grant(student))


def test():
    student_bachelor = create_bachelor('Vasua', '1011', 4)
    student_aspirant = create_aspirant('Petya', '12312', 3.21)
    print_students(student_bachelor, student_aspirant)
    student_aspirant = update_average_mark(student_aspirant, 5)
    student_bachelor = update_average_mark(student_bachelor, 4.48)
    print_students(student_bachelor, student_aspirant)


if __name__ == '__main__':
    test()
