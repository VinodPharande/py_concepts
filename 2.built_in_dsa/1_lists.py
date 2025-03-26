"""
data structures (lists, dictionaries, sets, tuples ?
Certainly, Vinod! Let’s break down these fundamental Python data structures, highlighting their characteristics and typical use cases:

1. Lists
Definition: Ordered and mutable (modifiable) collection of items.

Key Features:

Can contain items of different data types (e.g., integers, strings, etc.).

Elements are indexed (starting from 0).

Useful for storing sequential data, like a list of names or numbers.

Example:

python
my_list = [1, 2, 3, "hello", True]
my_list.append(4)  # Adds 4 to the end
my_list[0]         # Accesses the first item (1)
Common Methods: .append(), .remove(), .sort(), .pop().


1. Lists
Exercise 1: Create a list of 5 integers. Write a function to:

Add a new number at the end of the list.

Remove a specific number from the list (if it exists).

Sort the list in descending order.

Exercise 2: Take a list of words (e.g., ["apple", "banana", "cherry", "date"]) and:

Count how many words start with the letter "a."

Replace all occurrences of "banana" with "blueberry."
"""

def list_operations():
    my_list = [5, 10, 15, 20, 25]
    print("Original List:", my_list)
    
    # Add a number
    my_list.append(30)
    print("After Adding 30:", my_list)
    
    # Remove a specific number
    if 15 in my_list:
        my_list.remove(15)
    print("After Removing 15:", my_list)
    
    # Sort in descending order
    my_list.sort(reverse=True)
    print("Sorted List (Descending):", my_list)

def word_operations():
    words = ["apple", "banana", "cherry", "date", "avacado"]
    print("Original List:", words)
    
    # Count words starting with 'a'
    count_a = sum(1 for word in words if word.startswith("a"))
    print("Words starting with 'a':", count_a)
    
    # Replace 'banana' with 'blueberry'
    words = ["blueberry" if word == "banana" else word for word in words]
    print("After Replacement:", words)



list_operations()
word_operations()
