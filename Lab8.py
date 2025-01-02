# Program Name: Lab8.py
# Course: IT1114/Section BWE
# Student Name: Kendres Rhodes
# Assignment Number: Lab8
# Due Date: 10/20/2024
# Purpose: This program combines two integer arrays of random numbers, removes duplicates, and displays the unique numbers.
# List specific resources used to complete the assignment: CCSE tutoring center, Modules from Programming Principles lecture

import random

def main():
    # User insert a positive integer N greater than 1
    N = int(input("Enter a positive integer greater than 1: "))

    # N is greater than 1
    if N <= 1:
        print("Please enter a number greater than 1.")
        return

    # Create two arrays with N random integers between 0 and 500
    array1 = [random.randint(0, 500) for _ in range(N)]
    array2 = [random.randint(0, 500) for _ in range(N)]

    # Combine the two arrays and remove duplicates
    combined_array = list(set(array1) | set(array2))

    for i in range(len(combined_array)):
        for j in range(0, len(combined_array) - i - 1):
            if combined_array[j] > combined_array[j + 1]:
                # Swap if the element found is greater than the next element
                combined_array[j], combined_array[j + 1] = combined_array[j + 1], combined_array[j]

    # Output the contents of the final array
    print("The contents of the final array, one number per line:")
    for number in combined_array:
        print(number)


if __name__ == "__main__":
    main()
