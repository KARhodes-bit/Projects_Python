# Program Name: Lab10.py
# Course: IT1114/Section BWE
# Student Name: Kendres Rhodes
# Assignment Number: Lab10
# Due Date: 11/10/2024
# Purpose: This program defines a worker class that encapsulates data about an office worker, including employee number, office number, name, birthdate, and hours worked, with exception handling for invalid input.

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
        self.hourly_salary = 0.0
        self.overtime_salary = 0.0

    def get_employee_number(self):
        """Returns the employee number."""
        return self.employee_number

    def set_employee_number(self, x):
        """Sets the employee number; raises an exception if the input is not an integer."""
        if not isinstance(x, int):
            raise ValueError("Employee number must be an integer.")
        self.employee_number = x

    def get_office_number(self):
        """Returns the office number."""
        return self.office_number

    def set_office_number(self, x):
        """Sets the office number if within valid range (100-500); raises an exception if out of range."""
        if not (100 <= x <= 500):
            raise ValueError("Office number must be between 100 and 500.")
        self.office_number = x

    def get_name(self):
        """Returns the employee’s name."""
        return self.name

    def set_name(self, x):
        """Sets the employee’s name; raises an exception if the name is empty
        and removes invalid characters."""
        if not x:
            raise ValueError("Name cannot be empty.")
        # Remove unwanted characters
        self.name = x.replace('_', '').replace('.', '').replace('-', '')

    def get_birthdate(self):
        """Returns the employee's birthdate in MM/DD/YYYY format."""
        return f"{self.month}/{self.day}/{self.year}"

    def set_birthdate(self, m, d, y):
        """Validates the month, day, and year for birthdate; raises exceptions if invalid."""
        if not (1 <= m <= 12):
            raise ValueError("Month must be between 1 and 12.")
        if not (1 <= d <= 31):
            raise ValueError("Day must be between 1 and 31.")
        self.month = m
        self.day = d
        self.year = y

    def get_hours_worked(self):
        """Returns the number of hours worked."""
        return self.total_hours_worked

    def add_hours(self, x):
        """Adds hours worked; raises an exception if the input is negative
        and calculates overtime if hours exceed 9."""
        if x < 0:
            raise ValueError("Hours worked cannot be negative.")
        if x > 9:
            self.total_hours_worked += 9
            self.total_overtime_hours += (x - 9)
        else:
            self.total_hours_worked += x

    def get_hours_overtime(self):
        """Returns the number of overtime hours worked."""
        return self.total_overtime_hours

    def set_hourly_salary(self, x):
        """Sets the worker's hourly salary; raises an exception if the input is negative."""
        if x < 0:
            raise ValueError("Hourly salary cannot be negative.")
        self.hourly_salary = x

    def get_hourly_salary(self):
        """Returns the worker's hourly pay."""
        return self.hourly_salary

    def set_overtime_salary(self, x):
        """Sets the worker's overtime salary; raises an exception if the input is negative."""
        if x < 0:
            raise ValueError("Overtime salary cannot be negative.")
        self.overtime_salary = x

    def get_overtime_salary(self):
        """Returns the worker's overtime salary."""
        return self.overtime_salary

    def get_pay(self):
        """Returns the worker's total pay."""
        return (self.total_hours_worked * self.hourly_salary) + (self.total_overtime_hours * self.overtime_salary)
