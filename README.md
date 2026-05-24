# University Registration System

A Python program that simulates a university registration system for students and teachers. This system allows users to register new students and teachers with their personal information and academic details.

## Overview

This project demonstrates **object-oriented programming** concepts including inheritance, encapsulation, and polymorphism. The system manages two types of users: **Students** and **Teachers**, each inheriting from a base **Person** class.

## Features

- **Student Registration** — Register students with field of study, academic level, and average grade
- **Teacher Registration** — Register teachers with subjects, grade level, and hourly rate
- **Data Management** — Store and manage student and teacher information
- **Input Validation** — Comprehensive error handling and user input validation
- **User-Friendly Interface** — Interactive menu-driven system

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Project Structure

```
university-registration-system/
├── models/
│   ├── __init__.py
│   ├── person.py      # Parent class Person
│   ├── student.py     # Child class Student
│   └── teacher.py     # Child class Teacher
├── functions.py       # Registration functions
├── main.py            # Entry point
└── README.md
```

## Classes

- **Person** — Parent class with common attributes (name, firstname, age, is_active)
- **Student(Person)** — Child class with field, level, average, student_id
- **Teacher(Person)** — Child class with subjects, grade, hourly_rate, hours_per_week

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

## Usage Example

When you run the program, you'll see an interactive menu to:
1. Register a new student (with name, age, field, level, average, and student ID)
2. Register a new teacher (with name, age, subjects, grade, hourly rate, and hours per week)
3. View registered users
4. Exit the system

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