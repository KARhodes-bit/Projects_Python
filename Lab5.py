# Program Name: Lab5.py
# Course: IT1114/Section BWE
# Student Name: Kendres Rhodes
# Assignment Number: Lab5
# Due Date: 09/29/2024
# Purpose: This program prompts the user for a starting and ending number, and prints all prime numbers within that range inclusively.
# List specific resources used to complete the assignment:


def is_prime(num):
    """Check if a number is prime."""
    if num < 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:  # If a number is divisible by i then it is not prime
            return False
    return True  # If no number divisible by i then number is prime

# Get the starting and ending numbers from the user
starting_number = int(input("Starting Number: "))
ending_number = int(input("Ending Number: "))

# Check for prime numbers in the range
for num in range(starting_number, ending_number + 1):
    if is_prime(num):
        print(f"{num}")
