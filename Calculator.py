
# INTERACTIVE CALCULATOR & UNIT CONVERTER

# Function to get valid number input
def get_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input! Please enter a number.")


# 1. Addition
def addition():
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    print("Answer:", num1 + num2)


# 2. Subtraction
def subtraction():
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    print("Answer:", num1 - num2)


# 3. Multiplication
def multiplication():
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    print("Answer:", num1 * num2)


# 4. Division
def division():
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    if num2 == 0:
        print("Error! Cannot divide by zero.")
    else:
        print("Answer:", num1 / num2)


# 5. Kilometers to Miles
def km_to_miles():
    km = get_number("Enter kilometers: ")

    if km < 0:
        print("Distance cannot be negative.")
    else:
        miles = km * 0.621371
        print("Miles:", miles)


# 6. Celsius to Fahrenheit
def celsius_to_fahrenheit():
    celsius = get_number("Enter temperature in Celsius: ")

    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)


# Main program
def main():

    while True:

        print("\n================================")
        print("   INTERACTIVE CALCULATOR")
        print("================================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Kilometers to Miles")
        print("6. Celsius to Fahrenheit")
        print("7. Quit")
        print("================================")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            addition()

        elif choice == "2":
            subtraction()

        elif choice == "3":
            multiplication()

        elif choice == "4":
            division()

        elif choice == "5":
            km_to_miles()

        elif choice == "6":
            celsius_to_fahrenheit()

        elif choice == "7":
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid choice! Please select between 1 and 7.")


# Start the program
main()
