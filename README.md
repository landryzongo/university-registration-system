# University Registration System

A Python program that simulates a university registration system 
for students and teachers.

## Project Structure

uni-registration-system/
├── models/
│   ├── __init__.py
│   ├── person.py      # Parent class Person
│   ├── student.py     # Child class Student
│   └── teacher.py     # Child class Teacher
├── functions.py       # Registration functions
├── main.py            # Entry point
└── README.md

## Classes

- **Person** — parent class with common attributes (name, firstname, age, is_active)
- **Student(Person)** — child class with field, level, average, student_id
- **Teacher(Person)** — child class with subjects, grade, hourly_rate, hours_per_week

## Concepts Covered

- Inheritance with `super().__init__()`
- Magic method `__str__()`
- `@staticmethod` for student mention calculation
- Input validation with `while` loop and `try/except`
- Boolean handling with `.lower() == "yes"`
- f-strings for all output

## How to Run

```bash
python main.py
```

## Authors

| # | Name | Contribution |
|---|------|--------------|
| 1 | YABRE Amma | Person class |
| 2 | SAWADOGO Asseta | Student class |
| 3 | ZONGO P J Landry | Teacher class & README |
| 4 | SAWADOGO Sandrine | Registration functions |
| 5 | ZONGO P J Malkiram | Main function |

## Course

PRG1406 — Advanced Programming  
Burkina Institute of Technology | May 2026