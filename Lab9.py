# Program Name: Lab9.py
# Course: IT1114/Section BWE
# Student Name: Kendres Rhodes
# Assignment Number: Lab9
# Due Date: 11/03/2024
# Purpose: This program checks if a password meets specific criteria, including length, character types (upper and lower case letters, numbers, and special characters).
# List specific resources used to complete the assignment: Modules from Programming Principles lecture


def is_valid_password(password):
    if len(password) < 9:  # Check if the password is at least 9 characters long
        return False

    has_upper = False  # track the presence of uppercase letters
    has_lower = False  # track the presence of lowercase letters
    has_digit = False  # track the presence of digits
    has_special = False  # track the presence of special characters

    # Set of special characters that are allowedh
    special_characters = {'#', '!', '$', '_'}

    # search through each character in the password
    for char in password:
        if char.isupper():
            has_upper = True  # Found an uppercase letter
        elif char.islower():
            has_lower = True  # Found a lowercase letter
        elif char.isdigit():
            has_digit = True  # Found a digit
        elif char in special_characters:
            has_special = True  # Found a special character

    return has_upper and has_lower and has_digit and has_special


# Ask user to enter a password
user_password = input("Password: ")

# Validate the password
if is_valid_password(user_password):
    print("Valid Password")
else:
    print("Invalid Password")
