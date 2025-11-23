from datetime import datetime

#stduent id
student_id = ("elvnga1465")
print(f"{student_id} Spreadsheet Automation Menu")

# Define menu options in a list
print("choose a number from the following options: ")
menu_options = [
    "1. input data",
    "2. view current data",
    "3. generate report"
    ]

# Display menu using a for-loop
for option in menu_options:
    print(option)

# Ask the user for a choice
choice = input("please select a menu option (1-3): ")

# check if the choice is valid
valid_choices = ["1", "2", "3"]

if choice in valid_choices:
     # Get current date and time
     current_time = datetime.now()
     print(f"selected option:",choice)
     print("current date and time:", current_time)
else:
    print("Error: Invalid  choice selected.")
