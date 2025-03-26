"""
Comparison Table:
Data Structure	    Ordered	    Mutable	    Duplicates-Allowed	     Unique                 Use-Case
List	            Yes	        Yes	        Yes	                     Sequential             Data storage
Dictionary	        No	        Yes	        N/A                      (keys must be unique)	Data mapping (key-value pairs)
Set	                No	        Yes	        No	                     Unique elements        Mmathematical ops
Tuple	            Yes	        No	        Yes	                     Fixed data             Memory-efficient


Create a dictionary where the keys are strings (e.g., "list", "set") and the values are the corresponding Python data structures. For example:

Write a program to iterate through the dictionary and print the type of each value.
"""

def mixed_operations():
    my_data = {
        "list": [1, 2, 3],
        "set": {4, 5, 6},
        "tuple": (7, 8, 9)
    }
    
    for key, value in my_data.items():
        print(f"{key.capitalize()} -> Type: {type(value).__name__}, Value: {value}")

mixed_operations()
