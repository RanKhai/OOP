from .Student import create_student


def create_aspirant(name, group, average_mark):
    student = create_student(name, group, average_mark)
    student['student']['grade'] = 'aspirant'
    return student
