"""
3. Sets
Definition: Unordered and mutable collection of unique items.

Key Features:

Eliminates duplicates automatically.

Useful for operations like union, intersection, and difference.

Example:

python
my_set = {1, 2, 3, 3, 4}  # Duplicate 3 will be removed
my_set.add(5)  # Adds an item
my_set.remove(2)  # Removes an item
Common Methods: .add(), .remove(), .union(), .intersection().

Exercise 1: Given two sets:

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5, 6}

Write a function to:

Find the union, intersection, and difference between the two sets.

Check if set1 is a subset of set2.

Exercise 2: Create a set of random numbers from 1 to 10 and:

Add a new number to the set.

Remove a number from the set.

Check if a specific number (e.g., 5) is in the set.
"""


def set_operations():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    
    # Union
    print("Union:", set1.union(set2))
    
    # Intersection
    print("Intersection:", set1.intersection(set2))
    
    # Difference
    print("Difference (set1 - set2):", set1.difference(set2))
    
    # Subset check
    print("Is set1 a subset of set2?", set1.issubset(set2))

def set_modifications():
    my_set = {1, 2, 3, 4, 5}
    print("Original Set:", my_set)
    
    # Add a number
    my_set.add(6)
    print("After Adding 6:", my_set)
    
    # Remove a number
    my_set.remove(3)
    print("After Removing 3:", my_set)
    
    # Check if a number exists
    print("Is 5 in the set?", 5 in my_set)



set_operations()
set_modifications()
