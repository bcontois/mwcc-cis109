# Single line comment
'''multi line comment
multi line comment line 2
'''
print("Welcome to Temperature Converter!")

# Name Input
name = input("What is your name? ")
print(f"Hello, {name}! Let's convert some temperatures.")

# Menu Input

is_exit = False

while not is_exit:

    print("Menu:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

    choice = input("Enter your choice (1 or 2): ")

    if (choice == '1'):

        temp_F = input("Enter temperature in Fahrenheit: ")
        temp_C = (float(temp_F) - 32) * 5/9

        print(f"{temp_F} degrees Fahrenheit is equal to {temp_C} Celsius degrees")
        break

    elif (choice == '2'):

        temp_C = input("Enter temperature in Celsius: ")
        temp_F = (float(temp_C) * 9/5) + 32

        print(f"{temp_C} degrees Celsius is equal to {temp_F} Fahrenheit degrees")
        break

    else:
        print("Invalid choice. Please select 1 or 2.")

