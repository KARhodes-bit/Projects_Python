# Program Name: Lab1.py
# Course: IT1114/Section BWE Fall
# Student Name: Kendres Rhodes
# Assignment Number: Lab1
# Due Date: 08/25/2024
# Purpose: What does the program do (in a few sentences)? When executed, the program will request input from user, perform the required calculations, and then print the results for the total square feet, floating cost, tax amount, and total amount due.
# Module 1 and 2 class PowerPoint notes
# Place comments within your code explaining the programming segments

#Lab1.py

# Function used to calculate the cost of flooring
def calculate_flooring_cost(length, width, cost_per_sq_ft):

    # Calculate the total square feet
    area_square_feet = length * width

    #Calculate the cost of flooring
    flooring_cost = area_square_feet * cost_per_sq_ft

    # Calculate the tax amount (7% of the flooring cost)
    tax_rate = 0.07
    tax_amount = flooring_cost * tax_rate

    # Calculate the total amount due
    total_amount_due = flooring_cost + tax_amount

    return area_square_feet, flooring_cost, tax_amount, total_amount_due

def main():
    # Get User Input
    length = float(input("Room Length: "))
    width =  float(input("Room Width: "))
    cost_per_sq_ft = float(input("Cost per Sq. Foot: "))

# Cost Calculations
    area_square_feet, flooring_cost, tax, total_amount_due = calculate_flooring_cost(length, width, cost_per_sq_ft)

#Results
    print(f"Square feet: {area_square_feet}")
    print(f"Flooring: {flooring_cost}")
    print(f"Tax: {tax}")
    print(f"Total: {total_amount_due}")

if __name__ == "__main__":

    main()
