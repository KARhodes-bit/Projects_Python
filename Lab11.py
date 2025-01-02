# Program Name: Lab11.py
# Course: IT1114/Section BWE
# Student Name: Kendres Rhodes
# Assignment Number: Lab11
# Due Date: 11/17/2024
# Purpose: This program creates and modifies a text file called users.txt. It allows adding, updating, and removing usernames in the file.


# Function to create the 'users.txt' file if it does not exist
def create_file():
    try:
        with open("users.txt", "x") as file:  # 'x' mode creates the file if it doesn't exist
            pass  # File is created, but we don't need to write anything yet
    except FileExistsError:
        # If the file already exists, no action is needed
        pass

# Function to add a username to the file
def add_user(username):
    with open("users.txt", "a") as file:  # Open the file in append mode
        file.write(username + "\n")  # Write the username followed by a newline

# Function to update an old username with a new username
def update_user(old_username, new_username):
    # First, read the existing usernames from the file
    with open("users.txt", "r") as file:
        users = file.readlines()

    # Re-write the file with the updated usernames
    with open("users.txt", "w") as file:
        for user in users:
            # If the old username is found, replace it with the new one
            if user.strip() == old_username:
                file.write(new_username + "\n")
            else:
                file.write(user)  # Keep the other usernames unchanged

# Function to remove a username from the file
def remove_user(username):
    # Read the current usernames from the file
    with open("users.txt", "r") as file:
        users = file.readlines()

    # Re-write the file, excluding the removed username
    with open("users.txt", "w") as file:
        for user in users:
            if user.strip() != username:  # Skip the username to be removed
                file.write(user)


