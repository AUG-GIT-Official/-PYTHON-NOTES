"""
Python Lists: Dos and Don'ts
"""

# 1. DO: Use lists for ordered, mutable collections of elements.
# Lists are perfect when you need to store multiple values that might change.
my_list = [1, 2, 3, 4]
print("Example list:", my_list)

# DON'T: Use lists when order or mutability doesn't matter.
# If order or duplicates are not required, consider using a `set` for better performance.
my_set = set([1, 2, 2, 3])  # Automatically removes duplicates
print("Example set (no duplicates):", my_set)

# -------------------------------------

# 2. DO: Use indexing to access specific elements in a list.
fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])

# DON'T: Access elements using out-of-range indices.
# This will raise an IndexError.
try:
    print(fruits[5])  # Invalid index
except IndexError as e:
    print("Error:", e)

# -------------------------------------

# 3. DO: Use slicing to access sublists.
numbers = [0, 1, 2, 3, 4, 5]
print("Slice [1:4]:", numbers[1:4])  # Output: [1, 2, 3]

# DON'T: Modify the original list while iterating over it.
# This can lead to unexpected behavior.
for num in numbers[:]:  # Use a copy (numbers[:]) instead of modifying the original.
    if num % 2 == 0:
        numbers.remove(num)
print("Modified list (removed evens):", numbers)

# -------------------------------------

# 4. DO: Use `append()`, `insert()`, or `extend()` to add elements.
my_list.append(5)  # Add a single element at the end
my_list.extend([6, 7])  # Add multiple elements
my_list.insert(0, 0)  # Insert at the beginning
print("List after adding elements:", my_list)

# DON'T: Use `+=` to add non-iterable elements to a list.
try:
    my_list += 8  # This will raise an error.
except TypeError as e:
    print("Error:", e)

# -------------------------------------

# 5. DO: Use `remove()`, `pop()`, or `del` to delete elements.
my_list.remove(3)  # Remove by value
popped_item = my_list.pop(0)  # Remove by index and return the value
del my_list[-1]  # Delete the last element by index
print("List after removing elements:", my_list)

# DON'T: Try to remove an element that doesn’t exist.
# This will raise a ValueError.
try:
    my_list.remove(100)  # 100 is not in the list
except ValueError as e:
    print("Error:", e)

# -------------------------------------

# 6. DO: Use list comprehensions for concise and efficient list creation.
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# DON'T: Write overly complex list comprehensions.
# Readability is more important than compactness.
# Instead of this:
complex_list = [x**2 for x in range(10) if x % 2 == 0 if x > 4]
print("Complex list comprehension:", complex_list)
# Prefer this:
filtered_squares = [x**2 for x in range(10) if x % 2 == 0 and x > 4]
print("Filtered squares:", filtered_squares)

# -------------------------------------

# 7. DO: Use `in` to check for membership.
print("Is 4 in the list?", 4 in my_list)

# DON'T: Iterate through the list manually for membership checks.
# Avoid this inefficient method:
found = False
for item in my_list:
    if item == 4:
        found = True
print("Found manually:", found)

# -------------------------------------

# 8. DO: Use `len()` for list length and `sorted()` for sorting.
print("Length of list:", len(my_list))
print("Sorted list:", sorted(my_list))

# DON'T: Assume that modifying a list method (e.g., `sort()`) returns the sorted list.
# `sort()` modifies the list in place and returns None.
unsorted_list = [3, 1, 4, 2]
sorted_list = unsorted_list.sort()  # This returns None
print("Sorted list (in-place):", unsorted_list)
print("Incorrect assumption (returns None):", sorted_list)

# -------------------------------------

# 9. DO: Use `copy()` or `copy.deepcopy()` to avoid unintentional changes.
import copy
nested_list = [[1, 2], [3, 4]]
shallow_copy = nested_list.copy()
deep_copy = copy.deepcopy(nested_list)
nested_list[0][0] = 99  # Modifies only the original and shallow copy
print("Original list:", nested_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)

# DON'T: Use `=` to copy lists. It creates a reference, not a new object.
copied_list = nested_list  # Both point to the same list
nested_list.append([5, 6])
print("Copied list:", copied_list)  # Also reflects changes

# -------------------------------------

# 10. DO: Use lists for dynamic collections with flexible sizes.
dynamic_list = []
for i in range(5):
    dynamic_list.append(i)
print("Dynamic list:", dynamic_list)

# DON'T: Use lists for large, fixed-size collections.
# For better performance in such cases, consider using arrays (from the `array` module).

# -------------------------------------
# Final Note: Use the right data structure for the task. While lists are versatile, 
# they may not always be the optimal choice. For example, use sets for uniqueness 
# or dictionaries for key-value pairs.
