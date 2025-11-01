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

import re

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

def middle_chars(word):
    """Return the middle character(s) of a word using simple slicing.
    - odd length -> single middle char
    - even length -> two middle chars
    """
    n = len(word)
    if n == 0:
        return ""
    mid = n // 2
    if n % 2 == 1:
        return word[mid]
    return word[mid - 1 :mid + 1]

# --- simple regex-based alternative ---
def middle_chars_regex(word):
    """Return the middle character(s) using a single regex.
    Works for both odd (1 char) and even (2 chars) lengths.
    """
    L = len(word)
    if L == 0:
        return ""
    half = L // 2
    if L % 2 == 1:
        # e.g. for length 5, capture the 3rd char: ^.{2}(.).{2}$
        pattern = rf'^.{{{half}}}(.).{{{half}}}$'
    else:
        # e.g. for length 6, capture the middle two chars: ^.{2}(.{2}).{2}$
        left = half - 1
        pattern = rf'^.{{{left}}}(.{{2}}).{{{left}}}$'
    m = re.match(pattern, word)
    return m.group(1) if m else ""

# Demos (simplified: only compare slice vs regex middle methods)
def middle_and_like_demos():
    words = ["apple", "application", "puppy", "happy", "pppp", "map", "top"]
    print("Words:", words)

    for w in words:
        print(
            w,
            "-> middle (slice):", middle_chars(w),
            "| middle (regex):", middle_chars_regex(w)
        )

middle_and_like_demos()

list_operations()
# Original List: [5, 10, 15, 20, 25]
# After Adding 30: [5, 10, 15, 20, 25, 30]
# After Removing 15: [5, 10, 20, 25, 30]
# Sorted List (Descending): [30, 25, 20, 10, 5]
word_operations()
# Original List: ['apple', 'banana', 'cherry', 'date', 'avacado']
# Words starting with 'a': 2
# After Replacement: ['apple', 'blueberry', 'cherry', 'date', 'avacado']