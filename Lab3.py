#Program Name: Lab3.py
#COURSE: IT1114/ Section BWE
#Student Name: Kendres Rhodes
#Assignment Number: Lab 3
#Due date: September 8th 2024
#Purpose: This program calculates the total sales for a department, the number of employees, and the manager's bonus based off the sales goals and individual salesperson sales.
#Additional resources: Prior knowledge of loops, KSU tutoring center, and book python for beginners. Also a bit of information from Module 2 and 3.

def main():
    # variables for total sales, number of employees, and salesperson total
    total_sales = 0
    number_employees = 0
    salesperson_total = 0

    # Input monthly sales goal
    sales_goal = float(input("Sales goal: "))

    # This is where you create a loop for each salesperson's data
    while True:
        number_employees += 1 # This loop will count the employees each time the loop is true

        # Total sales for the current salesperson
        salesperson_total = 0

        # Input the weekly sales data for salesperson
        for week in range(1,5):
            # Sales for current week
            weekly_sales = float(input(f"Salesperson {number_employees} week {week}: "))
            salesperson_total += weekly_sales #All weekly sales

        # Add salesperson total to department total
        total_sales += salesperson_total

        # Ask user if there is another salesperson
        another = input("Another salesperson? (y/n): ").strip().lower()
        if another != 'y':
            break #This exit the loop if there aren't other salespersons


    # Calculate the manager's bonus using the total sales and sales goal

    if total_sales > sales_goal:
        manager_bonus = total_sales * 0.05
    else:
        manager_bonus = total_sales * 0.02

    # Display the results
    print (f"Number of Employees {number_employees}")
    print (f"Department Sales Goal {sales_goal }")
    print (f"Total Sales {total_sales }")
    print (f"Mgr. Bonus {manager_bonus }")

if __name__ == "__main__":
    main()


