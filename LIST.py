"""
Python Lists: A Complete Guide
"""

# 1. Definition of a List
# A list is a mutable, ordered collection of elements. 
# It can store elements of different data types and allows duplicates.

my_list = [10, "apple", 3.14, True]  # Example of a list
print("Example list:", my_list)

# 2. Creating a List
# Lists can be empty or contain multiple elements.
empty_list = []
numbers = [1, 2, 3, 4]
mixed_list = ["Hello", 42, 3.14, False]

print("Empty list:", empty_list)
print("Numbers list:", numbers)
print("Mixed data list:", mixed_list)

# 3. Accessing Elements
# Access elements using indexing (0-based) or negative indexing.
fruits = ["apple", "banana", "cherry"]
print("First element:", fruits[0])  # Indexing
print("Last element:", fruits[-1])  # Negative indexing

# 4. Slicing a List
# Slicing allows accessing a range of elements: list[start:stop:step].
numbers = [0, 1, 2, 3, 4, 5, 6]
print("Sliced list (1:4):", numbers[1:4])  # Output: [1, 2, 3]
print("Reversed list:", numbers[::-1])    # Output: [6, 5, 4, 3, 2, 1, 0]

# 5. Modifying Lists
# Lists are mutable, meaning you can change, add, or remove elements.
fruits[1] = "mango"  # Changing elements
print("Modified list:", fruits)

# Adding elements
fruits.append("orange")               # Add to the end
fruits.insert(1, "grape")             # Add at specific index
fruits.extend(["kiwi", "melon"])      # Add multiple elements
print("List after adding elements:", fruits)

# Removing elements
fruits.remove("mango")  # Remove by value
fruits.pop(0)           # Remove by index
del fruits[1]           # Delete specific index
print("List after removing elements:", fruits)

# 6. Iterating Through a List
# Using a for loop
for fruit in fruits:
    print("Fruit:", fruit)

# Using enumerate() to get index and value
for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")

# 7. List Operations
# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5]
combined = list1 + list2
print("Concatenated list:", combined)

# Repetition
repeated = [0] * 5
print("Repeated list:", repeated)

# Membership
print("Is 'apple' in fruits?", "apple" in fruits)

# 8. Built-in List Functions
numbers = [5, 1, 7, 3, 9]
print("Length of numbers list:", len(numbers))  # Number of elements
print("Minimum value:", min(numbers))          # Smallest element
print("Maximum value:", max(numbers))          # Largest element
print("Sum of elements:", sum(numbers))        # Sum of numeric elements
print("Sorted list:", sorted(numbers))         # Sorted copy of the list

# 9. List Methods
# Useful methods to manipulate lists
numbers.append(10)             # Add an element
numbers.sort()                 # Sort the list
numbers.reverse()              # Reverse the list
print("After append, sort, reverse:", numbers)

# 10. Nested Lists
# Lists can contain other lists as elements.
nested = [[1, 2, 3], [4, 5], [6]]
print("Nested list:", nested)
print("Access first list:", nested[0])
print("Access element in nested list:", nested[0][1])  # Access '2'

# 11. List Comprehensions
# Create lists in a concise way
squares = [x**2 for x in range(5)]  # Squares of 0 to 4
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # Squares of even numbers
print("Squares:", squares)
print("Even squares:", even_squares)

# 12. Copying Lists
# Copy a list without affecting the original
list1 = [1, 2, 3]
shallow_copy = list1.copy()  # Shallow copy
import copy
deep_copy = copy.deepcopy(nested)  # Deep copy for nested lists
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)

# 13. List vs Other Data Types
# Lists vs Tuples: Lists are mutable; tuples are immutable.
# Lists vs Sets: Lists allow duplicates; sets do not.
# Lists vs Dictionaries: Lists store individual elements; dictionaries store key-value pairs.
