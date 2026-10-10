#grocerylistapplication.py program
#Brian J Contois CIS109-G1 27 September 2026
#Introduction to Programming (Python)
#
#This program will allow a user to create a grocery list
#The user will be able to add items one by one, then display the list as a whole
#it will be able to count how many items are in the list 
#it will also be able to display the first and last item individually
#and allow the user to clear the list and start over
#there are error corrections in place to prevent a crash 
#if the user tries to display the first or last item when the list is empty

print("\n\n\n\n\n\n\n")

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
        item = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEnter an item to add to the shopping list: ")
        grocery_list.append(item)
        print("\n\n\n\n\n\n\n\n\n\n\n\n")

    elif(selection == "2"):
        print(f"\n\n\n\n\nYour Grocery List: {grocery_list}\n\n")

    elif(selection == "3"):
        print(f"\n\n\n\n\nItem Count: {len(grocery_list)}\n\n")

    elif(selection == "4"):
        if len(grocery_list) == 0:
            print("\n\n\n\n\nThe shopping list is empty.\n\n")
        else:
            print(f"\n\n\n\n\nFirst Item: {grocery_list[0]}\n\n")

    elif(selection == "5"):
        if len(grocery_list) == 0:
            print("\n\n\n\n\nThe shopping list is empty.\n\n")
        else:
            print(f"\n\n\n\n\nLast Item: {grocery_list[-1]}\n\n")

    elif(selection == "6"):
        grocery_list.clear()
        print("\n\n\n\n\nShopping list has been cleared.\n\n")

    elif(selection == "7"):
        print("\n\n\n\n\n\n\n\n\n\n\nOh No! Exiting the Program! G-O-O-D-B-Y-E-!-!-!\n\n\n\n\n\n\n\n\n\n\n\n")
        break
    else:
        print("\n\n\n\n\n\n\n\n\n\n\nInvalid selection, please try again.")
        input("Hit [enter] to continue...\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n")
        continue
##### 5:22PM 9/27/2026 Brian J Contois Final Version of Grocery List Application Program