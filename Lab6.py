# Program Name: Lab6.py
# Course: IT1114/Section BWE
# Student Name: Kendres Rhodes
# Assignment Number: Lab6
# Due Date: 10/06/2024
# Purpose: This program defines a worker class that encapsulates data about an office worker, including employee number, office number, name, birthdate, and hours worked.
# List specific resources used to complete the assignment:


class Worker:
    def __init__(self):
        """Constructor to initialize worker attributes."""
        self.employee_number = 0
        self.office_number = 0
        self.name = ""
        self.month = 0
        self.day = 0
        self.year = 0
        self.total_hours_worked = 0
        self.total_overtime_hours = 0

    def get_employee_number(self):
        """Returns the employee number."""
        return self.employee_number

    def set_employee_number(self, x):
        """Changes the employee number."""
        self.employee_number = x

    def get_office_number(self):
        """Returns the office number."""
        return self.office_number

    def set_office_number(self, x):
        """Sets the office number if within valid range (100-500)."""
        if 100 <= x <= 500:
            self.office_number = x
            return True
        else:
            return False

    def get_name(self):
        """Returns the employee’s name."""
        return self.name

    def set_name(self, x):
        """Changes the employee’s name."""
        self.name = x

    def get_birthdate(self):
        """Returns the employee's birthdate."""
        return self.month + "/" + self.day + "/" + self.year

    def set_birthdate(self, m, d, y):
        """Validates the month, day, and year for birthdate."""
        if not (1 <= m <= 12):
            return False
        if not (1 <= d <= 31):
            return False
        """Sets the employee's birthdate with validation."""
        self.day = d
        self.month = m
        self.year = y
        return True

    def get_hours_worked(self):
        """Returns the number of hours worked."""
        return self.total_hours_worked

    def add_hours(self, x):
        """Adds hours worked; calculates overtime if hours exceed 9."""
        if x > 9:
            self.total_hours_worked += 9
            self.total_overtime_hours += (x - 9)
        else:
            self.total_hours_worked += x

    def get_hours_overtime(self):
        """Returns the number of overtime hours worked."""
        return self.total_overtime_hours


