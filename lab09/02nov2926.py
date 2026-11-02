# Initial list
fruits = ["apple", "banana"]
# Appending a new item
fruits.append("cherry")
print(fruits)
# Output: ['apple', 'banana', 'cherry'

# Initial list
colors = ["red", "blue", "green", "blue"]
# Removing "blue"
colors.remove("blue")
print(colors)
# Output: ['red', 'green', 'blue'] (Notice only the first 'blue' is gone)

# Initial list
numbers = [10, 20, 30, 40]
# Example A: Pop the last item (Default)
last_item = numbers.pop()
print(f"Popped item: {last_item}") # Output: 40
print(f"List after pop: {numbers}") # Output: [10, 20, 30]
# Example B: Pop an item by index
# Let's reset the list for this example
numbers = [10, 20, 30]
second_item = numbers.pop(1) # Removes index 1
print(f"Popped item: {second_item}") # Output: 20
print(f"List after pop: {numbers}") # Output: [10, 30]


tasks = ["Write code", "Debug"]
# Insert "Plan project" at the very start
tasks.insert(0, "Plan project")
print(tasks)
# Output: ['Plan project', 'Write code', 'Debug']
# Inserting in the middle
# You can place an item anywhere by specifying its index.
grades = [85, 90, 95]
# Insert a 92 at index 1 (the second position)
grades.insert(1, 92)
print(grades)
# Output: [85, 92, 90, 95]

letters = ["A", "B", "C"]
# Index 100 is way beyond the list length
letters.insert(100, "Z")
print(letters)
# Output: ['A', 'B', 'C', 'Z'] (It just added it to the end)
# Index -1 is technically "before" the last item
letters.insert(-1, "X")
print(letters)
# Output: ['A', 'B', 'C', 'X', 'Z']

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I love eating {fruit}")
# Output:
# I love eating apple
# I love eating banana
# I love eating cherry


fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry


numbers = [1, 2, 3, 4, 5]
# Create a new list where every number is squared
squares = [n**2 for n in numbers]
print(squares)
# Output: [1, 4, 9, 16, 25]

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Position {i} contains {fruits[i]}")

    fruits = ["apple", "banana", "cherry"]
    i = 0
    while i < len(fruits) and i < 3:
        print(fruits[i])
        i += 1 
# Don't forget to increment, or you'll get an infinite loop!

numbers = [5, 2, 9, 1, 5, 8]
# Sorts the list in ascending order
numbers.sort()
print(f"Sorted In-place: {numbers}")
# Output: [1, 2, 5, 5, 8, 9]

numbers = [5, 2, 9, 1, 5, 8]
# Creates a new sorted list
new_list = sorted(numbers)
print(f"Original: {numbers}") # [5, 2, 9, 1, 5, 8]
print(f"New List: {new_list}") # [1, 2, 5, 5, 8, 9]

numbers = [1, 2, 3, 4, 5]
# Using .sort()
numbers.sort(reverse=True)
print(f"Descending In-place: {numbers}") # [5, 4, 3, 2, 1]
# Using sorted()
new_list = sorted(numbers, reverse=True)

fruits = ["apple", "banana", "cherry"]
reversed_fruits = fruits[::-1]
print(f"Original: {fruits}") # ['apple', 'banana', 'cherry']
print(f"Reversed Slicing: {reversed_fruits}") # ['cherry', 'banana','apple']

fruits = ["apple", "banana", "cherry"]
# reversed() returns an iterator, so we convert it back to a list
reversed_list = list(reversed(fruits))
print(f"Reversed Iterator: {reversed_list}")

numbers = [15, 8, 23, 4, 16, 42, 10]
# Find the largest value in the list
largest = max(numbers)
print("Largest value:", largest)

numbers = [15, 8, 23, 4, 16, 42, 10]
# Find the smallest value in the list
smallest = min(numbers)
print("Smallest value:", smallest)

numbers = [15, 8, 23, 4, 16, 42, 10]
# Calculate the sum of all values in the list
total = sum(numbers)
print("Total:", total)

