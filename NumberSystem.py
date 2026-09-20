number = int(input("Enter a positive integer with at least 3 digits: "))

# Check if the number is positive
if number <= 0:
    print("Please enter a positive number.")

# Check if the number has at least 3 digits
elif number < 100:
    print("Please enter a number with at least 3 digits.")

else:
    # Convert the number into different number systems
    binary = bin(number)
    octal = oct(number)
    hexadecimal = hex(number)

    # Find the last digit
    last_digit = number % 10

    # Check whether the number is even or odd
    if number % 2 == 0:
        result = "Even"
    else:
        result = "Odd"

    # Display results
    print("\n----- NUMBER ANALYSIS -----")
    print("Decimal:", number)
    print("Binary:", binary)
    print("Octal:", octal)
    print("Hexadecimal:", hexadecimal)
    print("Last Digit:", last_digit)
    print("Number Type:", result)
