class Person:
    def __init__(self, name, firstname, age, is_active):
        self.name = name
        self.firstname = firstname
        self.age = age
        self.is_active = is_active

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"First Name: {self.firstname}")
        print(f"Age: {self.age}")
        print(f"Active: {'Yes' if self.is_active else 'No'}")

    def __str__(self):
        return f"{self.firstname} {self.name}, Age: {self.age}, Active: {'Yes' if self.is_active else 'No'}"
    
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
class Teacher(Person):
    def __init__(self, name, firstname, age, is_active, subjects, grade, hourly_rate, hours_per_week):
        super().__init__(name, firstname, age, is_active)
        self.subjects = subjects
        self.grade = grade
        self.hourly_rate = hourly_rate
        self.hours_per_week = hours_per_week

    def display_courses(self):
        super().display_info()
        print(f"Subjects: {', '.join(self.subjects)}")
        print(f"Grade: {self.grade}")
        print(f"Hourly Rate: {self.hourly_rate}")
        print(f"Hours per Week: {self.hours_per_week}")
    def calculate_monthly_salary(self):
        return self.hourly_rate * self.hours_per_week * 4 