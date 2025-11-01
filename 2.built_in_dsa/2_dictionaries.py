"""
2. Dictionaries
Definition: Unordered and mutable collection of key-value pairs.

Key Features:

Keys are unique, while values can be duplicated.

Used for mapping or associating data (e.g., user profile: name -> "Vinod").

Example:

python
my_dict = {"name": "Vinod", "age": 30, "location": "Ilford"}
my_dict["age"]      # Accesses the value associated with the key 'age'
my_dict["hobby"] = "Coding"  # Adds a new key-value pair
Common Methods: .keys(), .values(), .items().

Exercise 1: Create a dictionary to store information about 3 students, where each key is the student’s name, and the value is their score. Write a function to:

Add a new student and score.

Update an existing student's score.

Find the student(s) with the highest score.

Exercise 2: Given a dictionary of fruits and their prices, e.g., {"apple": 2, "banana": 1, "cherry": 3}:

Write a function to find the total price of all fruits.

Add a new fruit to the dictionary, only if it doesn’t already exist.
"""


def student_scores():
    students = {"Alice": 85, "Bob": 90, "Charlie": 78}
    print("Original Dictionary:", students)
    
    # Add a new student
    students["David"] = 92
    print("After Adding David:", students)
    
    # Update a student's score
    students["Alice"] = 88
    print("After Updating Alice's Score:", students)
    
    # Find the highest score
    highest_score = max(students.values())
    top_students = [name for name, score in students.items() if score == highest_score]
    print("Top Student(s):", top_students, "with score", highest_score)

def fruit_prices():
    fruits = {"apple": 2, "banana": 1, "cherry": 3}
    print("Original Dictionary:", fruits)
    
    # Total price
    total_price = sum(fruits.values())
    print("Total Price of Fruits:", total_price)
    
    # Add a new fruit
    if "orange" not in fruits:
        fruits["orange"] = 4
    print("After Adding Orange:", fruits)

def sort_dictionary_demo():
    fruits = {"apple": 2, "banana": 1, "cherry": 3, "date": 2}
    print("Original dict:", fruits)

    # 1) Sorted list of tuples by key (alphabetical)
    by_key = sorted(fruits.items(), key=lambda kv: kv[0])
    print("Sorted by key (list of tuples):", by_key)
    # result: [('apple', 2), ('banana', 1), ('cherry', 3), ('date', 2)]
    print("Sorted by key (list of tuples):", dict(by_key))
    # result: {'apple': 2, 'banana': 1, 'cherry': 3, 'date': 2}

    # 2) Sorted list of tuples by value (ascending)
    by_value = sorted(fruits.items(), key=lambda kv: kv[1])
    print("Sorted by value (ascending):", by_value)
    # result: [('banana', 1), ('apple', 2), ('date', 2), ('cherry', 3)]
    print("Sorted by value (ascending):", dict(by_value))
    # result: {'banana': 1, 'apple': 2, 'date': 2, 'cherry': 3} 

    # 3) Sorted by value (descending)
    by_value_desc = sorted(fruits.items(), key=lambda kv: kv[1], reverse=True)
    print("Sorted by value (descending):", by_value_desc)

    # 4) Convert sorted list back to dict (new dict will preserve this order)
    dict_by_value = dict(by_value)
    print("New dict ordered by value (ascending):", dict_by_value)

    # 5) If you need an immutable ordered sequence, use tuple()
    tuple_by_key = tuple(by_key)
    print("Tuple of items sorted by key:", tuple_by_key)

    # 6) Examples: top N items by value
    top2 = sorted(fruits.items(), key=lambda kv: kv[1], reverse=True)[:2]
    print("Top 2 fruits by price:", top2)

def rename_key(d, old_key, new_key, overwrite=False):
    """
    Rename a single key in dict d.
    - If old_key not in d: KeyError.
    - If new_key exists and overwrite is False: ValueError.
    Returns the modified dict (in-place).
    """
    if old_key not in d:
        raise KeyError(f"Key not found: {old_key}")
    if new_key in d and not overwrite:
        raise ValueError(f"New key already exists: {new_key}")
    d[new_key] = d.pop(old_key)
    return d

def rename_keys_bulk(d, mapping, overwrite=False):
    """
    Rename multiple keys according to mapping {old_key: new_key}.
    Returns a NEW dict with keys renamed (does not modify original).
    If overwrite is False and mapping would cause collisions, raises ValueError.
    """
    # Build list of target keys to detect collisions
    target_keys = []
    for old, new in mapping.items():
        if old in d:
            target_keys.append(new)
    # detect collisions if not allowed (excluding cases where source->same target)
    if not overwrite:
        existing = set(d.keys())
        collisions = [k for k in target_keys if k in existing and k not in mapping.keys()]
        if collisions:
            raise ValueError(f"Collision with existing keys: {collisions}")

    # Build new dict
    new_dict = {}
    for k, v in d.items():
        if k in mapping and mapping[k] is not None:
            new_key = mapping[k]
            new_dict[new_key] = v
        else:
            new_dict[k] = v
    return new_dict

def rename_key_demo():
    d = {"a": 1, "b": 2, "c": 3}
    print("Original:", d)

    # Simple rename (in-place)
    rename_key(d, "a", "alpha")
    print("After rename_key in-place:", d)

    # Rename with overwrite allowed
    d2 = {"x": 9, "y": 8}
    print("Before overwrite demo:", d2)
    d2["z"] = 7
    # rename x -> z will overwrite z if overwrite=True
    rename_key(d2, "x", "z", overwrite=True)
    print("After rename_key with overwrite:", d2)

    # Bulk rename (returns new dict)
    src = {"one": 1, "two": 2, "three": 3}
    mapping = {"one": "1", "three": "3"}
    new_src = rename_keys_bulk(src, mapping)
    print("Bulk rename result (new dict):", new_src)
    print("Original unchanged:", src)

student_scores()
fruit_prices()
# Add demo call
sort_dictionary_demo()
# Add demo call
rename_key_demo()
