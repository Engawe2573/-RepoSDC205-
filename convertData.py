from datetime import datetime

def convertData(data, choice):
    # Conversion formulas:
    # F -> C: (F - 32) * 5/9
    # lbs -> kg: lbs / 2.205
    # in -> cm: in * 2.54
    if choice == 1:
        return (data - 32) * 5/9  # Convert Fahrenheit to Celsius
    elif choice == 2:
        return data / 2.205  # Convert pounds to kilograms
    elif choice == 3:
        return data * 2.54  # Convert inches to centimeters

# getInput() - handles data input loop
def getInput(choice):
    print("How many entries are you inputting?")
    num_entries = int(input())  # Number of entries to input

    for i in range(num_entries):
        print("\nEnter a date: \n")
        date_value = input()

        # Prompt based on choice
        if choice == 1:
            prompt = "Enter the highest temperature for the inputted date (°F): \n"
        elif choice == 2:
            prompt = "Enter the weight in pounds for the inputted date: \n"
        elif choice == 3:
            prompt = "Enter the rain amount in inches for the inputted date: \n"

        value = float(input(prompt))

        # Calling convertData() with the numerical value and expecting a converted float
        converted = convertData(value, choice)

        print(f"The following was saved at {datetime.now()}: ")
        print(f"Date: {date_value}, Original Value: {value}, Converted Value: {converted}")

# Main program
student_id = "elvng1465"
print(f"{student_id}'s Spreadsheet Automation Menu")
print("Choose a number from the following options")
print("1. Input Data")
print("2. View current Data")
print("3. Generate Report")

selection = int(input())

timestamp = datetime.now()
print(f"\nYou selected {selection} at {timestamp}")

if selection == 1:
    print("1. Temperature")
    print("2. Weight")
    print("3. Rain Amount")
    spreadsheet_choice = int(input())  # Prompt user for choice before calling getInput()

    if spreadsheet_choice in (1, 2, 3):
        getInput(spreadsheet_choice)  # Pass the selected choice as an argument to getInput
    else:
        print("Error: The chosen functionality is not implemented yet.")
else:
    print("Error: The chosen functionality is not implemented yet.")
