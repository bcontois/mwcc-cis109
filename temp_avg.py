temperatures = []

while(True):
    print("Select an option from the following:")
    menu = """
    1. Add a temperature
    2. List temperatures
    3. Calculate average temperature
    4. Exit
    """
    print(menu)
    selection = float(input("Enter a selection: "))
    if (type(selection) != float):
                print("Invalid input, please enter a number.")
                input("Hit [enter] to continue...")
                continue
    if (selection == 1):
        temperature = input("Enter a temperature: ")
        temperatures.append(temperature)
    elif (selection == 2):
        print(temperatures)
        input("Hit [enter] to continue...")
    elif (selection == 3):
        total = 0
        for temperature in temperatures:
            total += float(temperature)
        average = total / len(temperatures)
        print(f"The average temperature is: {average}")
        input("Hit [enter] to continue...")
    elif (selection == 4):
        print("goodbye!")
        exit()
    else:
        print("Invalid selection, please try again.")
        input("Hit [enter] to continue...")