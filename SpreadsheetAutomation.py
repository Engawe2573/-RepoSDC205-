# Elvnga1465 spreadsheet automation menu

from datetime import datetime

print("elvnga1465 Excel Spreadsheet Automation Menu")
print("Choose a number from the folllowing options")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores into a variable called user_choice.
user_choice = input("please select an option (1-3): ")

print("\nYou selectedoption:", user_choice)
print("The time and date is", str(datetime.now()))
