grocery_list = []

while(True):

    print(f"""
    Welcome to Your Shopping List!

    Please make a selection from one of the following options:
 
    1. Add an item to the shopping list.
    2. Display the shopping list.
    3. Display the item count.
    4. Display the first item in the shopping list.
    5. Display the last item in the shopping list.
    6. Clear the shopping list.
    7. Exit the program.
    """)

    selection = input("selection: ")

    if(selection == "1"):
        item = input("Enter an item to add to the shopping list: ")
        grocery_list.append(item)

    elif(selection == "2"):
        print(f"Your Grocery List: {grocery_list}")

    elif(selection == "3"):
        print(f"Item Count: {len(grocery_list)}")

    elif(selection == "4"):
        print(f"First Item: {grocery_list[0]}")

    elif(selection == "5"):
        print(f"Last Item: {grocery_list[-1]}")

    elif(selection == "6"):
        grocery_list.clear()
        print("Shopping list has been cleared.")

    elif(selection == "7"):
        print("Oh No! Exiting the Program! G-O-O-D-B-Y-E-!-!-!")
        break
    else:
        print("Invalid selection, please try again.")
        input("Hit [enter] to continue...")
        continue