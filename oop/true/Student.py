class Student:
    def __init__(self, name, group, average_mark):
        self.name = name
        self.group = group
        self.average_mark = average_mark

    def _get_grant(self, minimal, usual, maximum):
        if self.average_mark == 5:
            return maximum
        elif 4 <= self.average_mark < 5:
            return usual
        elif 3 <= self.average_mark < 4:
            return minimal
        else:
            return 0

    def update_average_mark(self, mark):
        self.average_mark = mark
