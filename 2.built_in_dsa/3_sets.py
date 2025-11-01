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

def sort_set_demo():
    # Note: sets are unordered. sorted() returns a new list (not a set).
    nums = {3, 1, 4, 2, 5}
    print("Original set (unordered):", nums)
    print("Sorted list from set:", sorted(nums))  # [1,2,3,4,5]
    print("Sorted descending:", sorted(nums, reverse=True))  # [5,4,3,2,1]

    words = {"banana", "apple", "cherry"}
    print("Sorted words (alphabetical):", sorted(words))  # ['apple','banana','cherry']
    print("Sorted words by length:", sorted(words, key=len))  # sort using key function

    pairs = {(1, 3), (2, 1), (1, 2)}
    # sorted tuples: sorts by first element, then second
    print("Sorted pairs:", sorted(pairs))  # [(1,2),(1,3),(2,1)]

    # If you need an ordered, immutable sequence, convert the sorted list to a tuple
    ordered_tuple = tuple(sorted(nums))
    print("Ordered tuple from set:", ordered_tuple)



set_operations()
# Union: {1, 2, 3, 4, 5, 6}
# Intersection: {3, 4}
# Difference (set1 - set2): {1, 2}
# Is set1 a subset of set2? False
set_modifications()
# Original Set: {1, 2, 3, 4, 5}
# After Adding 6: {1, 2, 3, 4, 5, 6}
# After Removing 3: {1, 2, 4, 5, 6}
# Is 5 in the set? True
sort_set_demo()
# Original set (unordered): {3, 1, 4, 2, 5}
# Sorted list from set: [1, 2, 3, 4, 5]
# Sorted descending: [5, 4, 3, 2, 1]
# Sorted words (alphabetical): ['apple','banana','cherry']
# Sorted words by length: ['apple','banana','cherry']
# Sorted pairs: [(1,2),(1,3),(2,1)]
# Ordered tuple from set: (1, 2, 3, 4, 5)

# set method
# .union(): Returns a new set with elements from both sets.
# .intersection(): Returns a new set with elements common to both sets.
# .difference(): Returns a new set with elements in the first set but not in the second set.
# .issubset(): Returns True if the set is a subset of another set.
# .add(): Adds an element to the set.
# .remove(): Removes an element from the set. Raises KeyError if the element is not found.
# 'in' keyword: Checks if an element is present in the set, returns True or False.

