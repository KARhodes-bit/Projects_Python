# Program Name: Lab12.py
# Course: IT1114/Section BWE
# Student Name: Kendres Rhodes
# Assignment Number: Lab12
# Due Date: 12/01/2024
# Purpose: This program reads the grades from the file, calculates the average score for each distinct section, and prints the average for each section based on letter grades.

# Grade conversion table:
grade_to_score = {
    'A': 100,
    'B': 89,
    'C': 79,
    'D': 74,
    'F': 69
}


def calculate_averages(filename):
    # A dictionary to store the total score and count of students per section
    section_scores = {}

    # Open the grades.txt file for reading
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into components (student ID, section number, and grade)
            parts = line.strip().split('\t')
            student_id, section, grade = parts[0], parts[1], parts[2]

            # Convert the letter grade to a numerical score
            score = grade_to_score.get(grade, 0)  # Default to 0 if grade is not in the table

            # If the section is already in the dictionary, update the total score and count
            if section not in section_scores:
                section_scores[section] = {'total_score': 0, 'count': 0}

            # Add the score to the section's total and increment the student count
            section_scores[section]['total_score'] += score
            section_scores[section]['count'] += 1

    # Calculate the average for each section and print the result
    for section, data in section_scores.items():
        total_score = data['total_score']
        count = data['count']
        average = total_score / count if count > 0 else 0  # Avoid division by zero
        print(f"Section {section} average: {average:.3f}")



if __name__ == "__main__":

    filename = 'grades.txt'

    calculate_averages(filename)
