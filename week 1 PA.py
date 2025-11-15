from datetime import datetime

#Ask the user for their name and studentId
name = input("Enter your name: ")
student_id = input("Enter your studnt ID: ")

#Ask for two whole numbers
num1 = int(input("Enter the first whole number: "))
num2 = int(input("Enter the second whole number: "))

# perform three math calculations
addition = num1 + num2
multiplication = num1 * num2
division = num1 / num2

# output the result formattted to two decimal place
print("Addition result: {:.2f}".format(addition))
print("Multiplication result: {:.2f}".format(multiplication))
print("Division result: {:.2f}".format(division))


#Determine if the first number is larger or smaller
if num1 > num2:
    print("The first number is larger than the second number.")
elif num1 < num2:
    print("The first number is smaller than the second number.")
else:
    print("Both numbers are equal.")


#output user name and student Id
print("Name:", name)
print("student ID:", student_id)

#print system date and time to match screenshot requirement
print("\nCurrent Date and Time:", datetime.now())
