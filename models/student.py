from .person import Person

class Student(Person):
    def __init__(self, name, firstname, age, is_active, field, level, average, student_id):
        super().__init__(name, firstname, age, is_active)
        self.student_id = student_id
        self.field = field
        self.level = level
        self.average = average

    def is_admitted(self):
        return self.average >= 10

    @staticmethod
    def mention(average):
        if average >= 16:
            return "Excellent"
        elif average >= 14:
            return "Very Good"
        elif average >= 12:
            return "Good"
        elif average >= 10:
            return "Passable"
        else:
            return "Fail"
