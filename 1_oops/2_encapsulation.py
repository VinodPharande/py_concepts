"""
Encapsulation:
- Encapsulation is the process of restricting access to certain components of an object.
- It is used to prevent unauthorized access to the internal state of an object.
- In Python, encapsulation can be achieved by using private attributes and methods.
- Private attributes and methods are denoted by a double underscore prefix (__) in their names.
- Private attributes and methods are not accessible from outside the class.
- However, they can be accessed within the class itself.
- Encapsulation helps in data hiding and prevents accidental modification of data.

Key Points:
- Encapsulation is the bundling of data (attributes) and methods (functions) that operate on that data into a single unit (a class).
- It helps to protect data from unauthorized access and modification.
- In Python, this is achieved by using access modifiers (though Python's access modifiers are different than other languages).
"""

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Using a single underscore for "protected"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance()) #output 1500