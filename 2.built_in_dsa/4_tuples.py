"""
4. Tuples
Definition: Ordered and immutable (cannot be modified after creation) collection of items.

Key Features:

Often used for fixed data, like coordinates or database records.

More memory-efficient than lists.

Example:

python
my_tuple = (10, 20, "Vinod")
my_tuple[0]  # Accesses the first element (10)
Common Methods: .count(), .index().


Exercise 1: Create a tuple with 5 numbers (e.g., (10, 20, 30, 40, 50)). Write functions to:

Find the index of a specific number (e.g., 30).

Count how many times a given number appears in the tuple.

Exercise 2: Given a tuple coordinates = (4, 5), swap the values so it becomes (5, 4).
"""


def tuple_operations():
    my_tuple = (10, 20, 30, 40, 50)
    print("Original Tuple:", my_tuple)
    
    # Find index of 30
    index_30 = my_tuple.index(30)
    print("Index of 30:", index_30)
    
    # Count occurrences of a number
    count_10 = my_tuple.count(10)
    print("Count of 10:", count_10)

def swap_coordinates():
    coordinates = (4, 5)
    print("Original Tuple:", coordinates)
    
    # Swap values
    swapped = (coordinates[1], coordinates[0])
    print("Swapped Tuple:", swapped)


tuple_operations()
swap_coordinates()
