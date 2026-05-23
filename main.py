from models import Person, Student, Teacher
from functions import register_student, register_teacher


def show_menu():
    print("\n" + "="*50)
    print("SYSTEME D'INSCRIPTION UNIVERSITAIRE")
    print("="*50)
    print("1. Enregistrer un etudiant")
    print("2. Enregistrer un professeur")
    print("3. Voir les etudiants")
    print("4. Voir les professeurs")
    print("5. Quitter")
    print("="*50)
    choice = input("Choix: ")
    return choice


def main():
    students = []
    teachers = []
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            student = register_student()
            students.append(student)
            print(f"Etudiant {student.firstname} {student.name} enregistre!")
        
        elif choice == "2":
            teacher = register_teacher()
            teachers.append(teacher)
            print(f"Professeur {teacher.firstname} {teacher.name} enregistre!")
        
        elif choice == "3":
            if len(students) == 0:
                print("Pas d'etudiants!")
            else:
                print("\n" + "="*50)
                print("LISTE DES ETUDIANTS")
                print("="*50)
                for student in students:
                    print()
                    student.display_info()
                    print(f"ID: {student.student_id}")
                    print(f"Field: {student.field}")
                    print(f"Level: {student.level}")
                    print(f"Average: {student.average}")
                    print(f"Admitted: {'Yes' if student.is_admitted() else 'No'}")
                    print(f"Mention: {Student.mention(student.average)}")
        
        elif choice == "4":
            if len(teachers) == 0:
                print("Pas de professeurs!")
            else:
                print("\n" + "="*50)
                print("LISTE DES PROFESSEURS")
                print("="*50)
                for teacher in teachers:
                    print()
                    teacher.display_courses()
                    salary = teacher.calculate_monthly_salary()
                    print(f"Monthly Salary: {salary} FCFA")
        
        elif choice == "5":
            print("Au revoir!")
            break
        
        else:
            print("Choix invalide!")


if __name__ == "__main__":
    main()
