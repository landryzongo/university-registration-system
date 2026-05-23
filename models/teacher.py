from .person import Person

class Teacher(Person):
    def __init__(self, name, firstname, age, is_active, subjects, grade, hourly_rate, hours_per_week):
        super().__init__(name, firstname, age, is_active)
        self.subjects = subjects
        self.grade = grade
        self.hourly_rate = hourly_rate
        self.hours_per_week = hours_per_week

    def display_courses(self):
        self.display_info()
        print(f"Subjects: {', '.join(self.subjects)}")
        print(f"Grade: {self.grade}")
        print(f"Hourly Rate: {self.hourly_rate}")
        print(f"Hours per Week: {self.hours_per_week}")

    def calculate_monthly_salary(self):
        return self.hourly_rate * self.hours_per_week * 4
