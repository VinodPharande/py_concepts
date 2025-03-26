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



student_scores()
fruit_prices()
