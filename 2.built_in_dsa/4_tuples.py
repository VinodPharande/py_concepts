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

# New helpers demonstrating add/remove/edit (tuples are immutable)
def add_to_tuple(tpl, value, position=None):
    """
    Add value to tuple.
    - If position is None, append (using concatenation).
    - If position is an int, insert at that index (convert to list).
    Returns a new tuple.
    """
    if position is None:
        return tpl + (value,)
    # insert via list conversion
    lst = list(tpl)
    lst.insert(position, value)
    return tuple(lst)

def remove_from_tuple(tpl, value=None, index=None):
    """
    Remove by value or index. Returns a new tuple.
    - If value is provided, removes first occurrence.
    - If index is provided, removes element at that index.
    """
    lst = list(tpl)
    if index is not None:
        lst.pop(index)
        return tuple(lst)
    if value is not None:
        lst.remove(value)  # raises ValueError if not found
        return tuple(lst)
    raise ValueError("Either value or index must be provided.")

def edit_tuple(tpl, index, new_value):
    """
    Replace element at index with new_value. Returns a new tuple.
    """
    lst = list(tpl)
    lst[index] = new_value
    return tuple(lst)

# Demos
"""Tuples are immutable: you cannot change them in-place.
To add/remove/edit elements, either:
Convert to a list, modify, then convert back to a tuple (recommended for multiple/positioned edits).
Create a new tuple using concatenation/slicing (useful for simple add/remove/replace).
"""
def tuple_modify_demos():
    t = (1, 2, 3)
    print("Start:", t)

    # Add examples
    t_appended = add_to_tuple(t, 4)
    print("Appended 4:", t_appended)

    t_inserted = add_to_tuple(t, 0, position=0)
    print("Inserted 0 at pos 0:", t_inserted)

    # Remove examples
    t_removed_by_value = remove_from_tuple(t_appended, value=2)
    print("Removed value 2:", t_removed_by_value)

    t_removed_by_index = remove_from_tuple(t_appended, index=0)
    print("Removed index 0:", t_removed_by_index)

    # Edit example
    t_edited = edit_tuple(t, 1, 99)
    print("Edited index 1 -> 99:", t_edited)

    # Using concatenation/slicing directly (no list conversion)
    t = (1, 2, 3, 4)
    t_without_2 = t[:1] + t[2:]  # remove element at index 1
    print("Removed index 1 via slicing:", t_without_2)

def list_tuple_order_demo():
    # Lists and tuples preserve insertion order by default — they are NOT sorted automatically.
    lst = [3, 1, 2]
    print("Original list (insertion order):", lst)
    # result: [3, 1, 2]

    # sorted() returns a new list, does not modify the original
    print("sorted(lst) ->", sorted(lst))
    # result: [1, 2, 3]
    print("After sorted(), original list is unchanged:", lst)
    # result: [3, 1, 2]

    # list.sort() sorts in-place and returns None
    lst.sort()
    print("After lst.sort() (in-place):", lst)
    # result: [1, 2, 3]

    # Tuples are immutable — cannot sort in-place
    tpl = (3, 1, 2)
    print("Original tuple (insertion order):", tpl)
    # result: (3, 1, 2)
    print("sorted(tpl) ->", sorted(tpl))              # returns a list
    # result: [1, 2, 3]
    print("tuple(sorted(tpl)) ->", tuple(sorted(tpl)))  # ordered tuple from sorted result
    # result: (1, 2, 3)
    # Summary prints
    print("Note: insertion order != sorted order. Apply sorting explicitly when needed.")

# Add demo call
list_tuple_order_demo()

tuple_operations()
swap_coordinates()
tuple_modify_demos()
