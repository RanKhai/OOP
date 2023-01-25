from .Student import create_student


def create_bachelor(name, group, average_mark):
    student = create_student(name, group, average_mark)
    student['student']['grade'] = 'bachelor'
    return student
