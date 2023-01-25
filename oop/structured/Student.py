def create_student(name, group, average_mark):
    return {
        'student': {
            'name': name,
            'group': group,
            'average_mark': average_mark
        }
    }


def _get_grant(average_mark, minimum, usual, maximum):
    if average_mark == 5:
        return maximum
    elif 4 <= average_mark < 5:
        return usual
    elif 3 <= average_mark < 4:
        return minimum
    else:
        return 0


def get_grant(student):
    match student['student']['grade']:
        case 'bachelor':
            return _get_grant(student['student']['average_mark'], 1500, 2000, 3000)
        case 'aspirant':
            return _get_grant(student['student']['average_mark'], 3500, 4500, 5000)
        case _:
            return NotImplemented


def update_average_mark(student, mark):
    student['student']['average_mark'] = mark
    return student
