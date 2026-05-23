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
    def __init__(
        self, name, firstname, age, is_active, field, level, average, student_id
    ):
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
    def __init__(
        self,
        name,
        firstname,
        age,
        is_active,
        subjects,
        grade,
        hourly_rate,
        hours_per_week,
    ):
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

    
    

def register_student():
    """Creates a new student by asking the user for information"""

    # Get first name
    firstname = input("Enter first name: ")

    # Get last name
    name = input("Enter last name: ")

    # Get age - validate that it's a number
    age = None
    while age is None:
        try:
            age_input = input("Enter age: ")
            age = int(age_input)
        except ValueError:
            print("Error: age must be a number")

    # Get is_active - yes or no
    is_active = None
    while is_active is None:
        answer = input("Is the student active? (yes/no): ")
        if answer.lower() == "yes":
            is_active = True
        elif answer.lower() == "no":
            is_active = False
        else:
            print("Error: answer yes or no")

    # Get field
    field = input("Enter field of study: ")

    # Get level
    level = input("Enter level: ")

    # Get average - validate that it's a number
    average = None
    while average is None:
        try:
            average_input = input("Enter average (0-20): ")
            average = float(average_input)
        except ValueError:
            print("Error: average must be a number")

    # Get student ID - validate that it's a number
    student_id = None
    while student_id is None:
        try:
            student_id_input = input("Enter student ID: ")
            student_id = int(student_id_input)
        except ValueError:
            print("Error: student ID must be a number")

    # Create and return the Student object
    student = Student(
        name, firstname, age, is_active, field, level, average, student_id
    )
    return student
