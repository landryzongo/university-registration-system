def register_student():
    print("\n=== Enregistrer un etudiant ===")
    firstname = input("First name: ")
    name = input("Last name: ")
    
    age = None
    while age is None:
        try:
            age = int(input("Age: "))
            if age < 0:
                print("Age must be positive")
                age = None
        except ValueError:
            print("Age must be a number")

    is_active = None
    while is_active is None:
        answer = input("Active? (yes/no): ")
        if answer.lower() == "yes":
            is_active = True
        elif answer.lower() == "no":
            is_active = False
        else:
            print("Answer yes or no")

    field = input("Field: ")
    level = input("Level: ")
    
    average = None
    while average is None:
        try:
            average = float(input("Average (0-20): "))
            if average < 0 or average > 20:
                print("Average must be between 0 and 20")
                average = None
        except ValueError:
            print("Average must be a number")

    student_id = input("Student ID: ")

    from models import Student
    student = Student(name, firstname, age, is_active, field, level, average, student_id)
    return student


def register_teacher():
    print("\n=== Enregistrer un professeur ===")
    firstname = input("First name: ")
    name = input("Last name: ")
    
    age = None
    while age is None:
        try:
            age = int(input("Age: "))
            if age < 0:
                print("Age must be positive")
                age = None
        except ValueError:
            print("Age must be a number")

    is_active = None
    while is_active is None:
        answer = input("Active? (yes/no): ")
        if answer.lower() == "yes":
            is_active = True
        elif answer.lower() == "no":
            is_active = False
        else:
            print("Answer yes or no")

    subjects_input = input("Subjects (comma separated): ")
    subjects = [s.strip() for s in subjects_input.split(",")]

    grade = input("Grade (Vacataire/Assistant/Maitre-assistant): ")

    hourly_rate = None
    while hourly_rate is None:
        try:
            hourly_rate = float(input("Hourly rate: "))
            if hourly_rate < 0:
                print("Hourly rate must be positive")
                hourly_rate = None
        except ValueError:
            print("Hourly rate must be a number")

    hours_per_week = None
    while hours_per_week is None:
        try:
            hours_per_week = int(input("Hours per week: "))
            if hours_per_week < 0:
                print("Hours per week must be positive")
                hours_per_week = None
        except ValueError:
            print("Hours per week must be a number")

    from models import Teacher
    teacher = Teacher(name, firstname, age, is_active, subjects, grade, hourly_rate, hours_per_week)
    return teacher
def register_student():
    print("\n=== Enregistrer un etudiant ===")
    
    # Get basic information
    firstname = input("First name: ")
    name = input("Last name: ")
    
    # Get and validate age (must be a positive integer)
    age = None
    while age is None:
        try:
            age = int(input("Age: "))
            if age < 0:
                print("Age must be positive")
                age = None
        except ValueError:
            print("Age must be a number")

    # Get active status (yes/no only)
    is_active = None
    while is_active is None:
        answer = input("Active? (yes/no): ")
        if answer.lower() == "yes":
            is_active = True
        elif answer.lower() == "no":
            is_active = False
        else:
            print("Answer yes or no")

    # Get field of study and level
    field = input("Field: ")
    level = input("Level: ")
    
    # Get and validate average grade (must be between 0 and 20)
    average = None
    while average is None:
        try:
            average = float(input("Average (0-20): "))
            if average < 0 or average > 20:
                print("Average must be between 0 and 20")
                average = None
        except ValueError:
            print("Average must be a number")

    # Get student ID number
    student_id = input("Student ID: ")

    # Create and return the student object
    from models import Student
    student = Student(name, firstname, age, is_active, field, level, average, student_id)
    return student


def register_teacher():
    print("\n=== Enregistrer un professeur ===")
    
    # Get basic information
    firstname = input("First name: ")
    name = input("Last name: ")
    
    # Get and validate age (must be a positive integer)
    age = None
    while age is None:
        try:
            age = int(input("Age: "))
            if age < 0:
                print("Age must be positive")
                age = None
        except ValueError:
            print("Age must be a number")

    # Get active status (yes/no only)
    is_active = None
    while is_active is None:
        answer = input("Active? (yes/no): ")
        if answer.lower() == "yes":
            is_active = True
        elif answer.lower() == "no":
            is_active = False
        else:
            print("Answer yes or no")

    # Get subjects taught, split by commas and converted into a list
    subjects_input = input("Subjects (comma separated): ")
    subjects = [s.strip() for s in subjects_input.split(",")]

    # Get teacher grade/rank
    grade = input("Grade (Vacataire/Assistant/Maitre-assistant): ")

    # Get and validate hourly rate (must be positive)
    hourly_rate = None
    while hourly_rate is None:
        try:
            hourly_rate = float(input("Hourly rate: "))
            if hourly_rate < 0:
                print("Hourly rate must be positive")
                hourly_rate = None
        except ValueError:
            print("Hourly rate must be a number")

    # Get and validate hours per week (must be a positive integer)
    hours_per_week = None
    while hours_per_week is None:
        try:
            hours_per_week = int(input("Hours per week: "))
            if hours_per_week < 0:
                print("Hours per week must be positive")
                hours_per_week = None
        except ValueError:
            print("Hours per week must be a number")

    # Create and return the teacher object
    from models import Teacher
    teacher = Teacher(name, firstname, age, is_active, subjects, grade, hourly_rate, hours_per_week)
    return teacher