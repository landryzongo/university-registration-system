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
    firstname = None
    while not firstname:
        firstname = input("Enter first name: ").strip()
        if not firstname:
            print("Error: first name cannot be empty")

    # Get last name
    name = None
    while not name:
        name = input("Enter last name: ").strip()
        if not name:
            print("Error: last name cannot be empty")

    # Get age - validate that it's a positive number
    age = None
    while age is None:
        try:
            age_input = input("Enter age: ")
            age = int(age_input)
            if age < 0:
                print("Error: age must be positive")
                age = None
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
    field = None
    while not field:
        field = input("Enter field of study: ").strip()
        if not field:
            print("Error: field cannot be empty")

    # Get level
    level = None
    while not level:
        level = input("Enter level: ").strip()
        if not level:
            print("Error: level cannot be empty")

    # Get average - validate that it's a number between 0-20
    average = None
    while average is None:
        try:
            average_input = input("Enter average (0-20): ")
            average = float(average_input)
            if average < 0 or average > 20:
                print("Error: average must be between 0 and 20")
                average = None
        except ValueError:
            print("Error: average must be a number")

    # Get student ID - validate that it's a positive number
    student_id = None
    while student_id is None:
        try:
            student_id_input = input("Enter student ID: ")
            student_id = int(student_id_input)
            if student_id < 0:
                print("Error: student ID must be positive")
                student_id = None
        except ValueError:
            print("Error: student ID must be a number")

    # Create and return the Student object
    student = Student(
        name, firstname, age, is_active, field, level, average, student_id
    )
    return student


def register_teacher():
    """Creates a new teacher by asking the user for information"""

    # Get first name
    firstname = None
    while not firstname:
        firstname = input("Enter first name: ").strip()
        if not firstname:
            print("Error: first name cannot be empty")

    # Get last name
    name = None
    while not name:
        name = input("Enter last name: ").strip()
        if not name:
            print("Error: last name cannot be empty")

    # Get age - validate that it's a positive number
    age = None
    while age is None:
        try:
            age_input = input("Enter age: ")
            age = int(age_input)
            if age < 0:
                print("Error: age must be positive")
                age = None
        except ValueError:
            print("Error: age must be a number")

    # Get is_active - yes or no
    is_active = None
    while is_active is None:
        answer = input("Is the teacher active? (yes/no): ")
        if answer.lower() == "yes":
            is_active = True
        elif answer.lower() == "no":
            is_active = False
        else:
            print("Error: answer yes or no")

    # Get subjects - list of strings
    subjects = None
    while not subjects:
        subjects_input = input("Enter subjects separated by comma (ex: Python, Networks): ")
        subjects = [subject.strip() for subject in subjects_input.split(",")]
        if not subjects or all(not s for s in subjects):
            print("Error: subjects cannot be empty")
            subjects = None

    # Get grade - choice between Vacataire, Assistant, Maitre-assistant
    grade = None
    valid_grades = ["vacataire", "assistant", "maitre-assistant"]
    while grade is None:
        grade_input = input("Enter grade (Vacataire/Assistant/Maitre-assistant): ").lower()
        if grade_input in valid_grades:
            grade = grade_input
        else:
            print("Error: grade must be Vacataire, Assistant, or Maitre-assistant")

    # Get hourly rate - validate that it's a positive number
    hourly_rate = None
    while hourly_rate is None:
        try:
            hourly_rate_input = input("Enter hourly rate: ")
            hourly_rate = float(hourly_rate_input)
            if hourly_rate < 0:
                print("Error: hourly rate must be positive")
                hourly_rate = None
        except ValueError:
            print("Error: hourly rate must be a number")

    # Get hours per week - validate that it's a positive number
    hours_per_week = None
    while hours_per_week is None:
        try:
            hours_input = input("Enter hours per week: ")
            hours_per_week = int(hours_input)
            if hours_per_week < 0:
                print("Error: hours per week must be positive")
                hours_per_week = None
        except ValueError:
            print("Error: hours per week must be a number")

    # Create and return the Teacher object
    teacher = Teacher(
        name, firstname, age, is_active, subjects, grade, hourly_rate, hours_per_week
    )
    return teacher


def main():
    """Main function to run the registration system"""
    
    print("=" * 60)
    print("WELCOME TO THE UNIVERSITY REGISTRATION SYSTEM")
    print("=" * 60)
    
    # Register a student
    print("\n--- STUDENT REGISTRATION ---")
    student = register_student()
    
    # Register a teacher
    print("\n--- TEACHER REGISTRATION ---")
    teacher = register_teacher()
    
    # Display summary
    print("\n" + "=" * 60)
    print("REGISTRATION SUMMARY")
    print("=" * 60)
    
    # Student information
    print("\n--- STUDENT INFORMATION ---")
    student.display_info()
    print(f"Student ID: {student.student_id}")
    print(f"Field of Study: {student.field}")
    print(f"Level: {student.level}")
    print(f"Average: {student.average}")
    print(f"Admitted: {'Yes' if student.is_admitted() else 'No'}")
    print(f"Performance: {Student.mention(student.average)}")
    
    # Teacher information
    print("\n--- TEACHER INFORMATION ---")
    teacher.display_courses()
    monthly_salary = teacher.calculate_monthly_salary()
    print(f"Monthly Salary: {monthly_salary:,.0f} FCFA")
    
    print("\n" + "=" * 60)
    print("END OF REGISTRATION")
    print("=" * 60)


if __name__ == "__main__":
    main()
