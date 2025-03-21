"""
Abstraction using Encapsulation and Interfaces
- Abstraction is the process of hiding the implementation details of an object and showing only the essential features of the object.
- Encapsulation is the bundling of data (attributes) and methods (functions) that operate on that data into a single unit (a class).
- Interfaces define a common set of methods that classes must implement.
- In Python, abstraction can be achieved by using encapsulation and interfaces.
- Encapsulation helps in data hiding and prevents unauthorized access to the internal state of an object.
- Interfaces define a common set of methods that classes must implement, allowing objects of different classes to be treated as objects of a common type.
- Abstraction, encapsulation, and interfaces are fundamental concepts in object-oriented programming (OOP).
- In the example below, the DataProcessor class is an interface with an abstract method process_data().
- The CSVProcessor and DatabaseProcessor classes are concrete implementations of the DataProcessor interface.
- The process_data() method in each class performs specific data processing tasks (reading a CSV file or querying a database).
- The analyze_data() function takes a DataProcessor object as an argument and calls its process_data() method.
- We can pass either a CSVProcessor or DatabaseProcessor object to the analyze_data() function, demonstrating abstraction in action.
- The analyze_data() function does not need to know the specific implementation details of the DataProcessor object; it only needs to know that the object has a process_data() method.

- This allows us to write more flexible and reusable code by decoupling the code that uses an object from the object's specific implementation.
- Abstraction, encapsulation, and interfaces help in reducing code complexity, increasing code reusability, and improving code maintainability.
- By using these concepts, we can create more modular, extensible, and scalable software systems.
- Abstraction, encapsulation, and interfaces are key principles of object-oriented design and are widely used in software development.
- Understanding these concepts is essential for writing clean, efficient, and maintainable code.
- By applying abstraction, encapsulation, and interfaces in our code, we can build robust and flexible software systems that are easier to understand, modify, and extend.
- These concepts are fundamental building blocks of object-oriented programming and are used in many programming languages, including Python.
- By mastering these concepts, we can become better software developers and create high-quality, well-structured code that meets the needs of users and stakeholders.
"""

class DataProcessor:  # Interface (implicitly defined by method signatures)
    def process_data(self):
        print("Processing data...")  # Abstract method (no implementation)
        pass

class CSVProcessor(DataProcessor):
    def __init__(self, filepath):
        self._filepath = filepath  # Encapsulated attribute

    def process_data(self):
        print("Reading CSV file...")  # Concrete method (with implementation)
        try:
            with open(self._filepath, 'r') as file:
                data = file.readlines()
                # Simulate data processing (e.g., cleaning, analysis)
                processed_data = [line.strip().upper() for line in data]
                return processed_data
        except FileNotFoundError:
            return "File not found."

class DatabaseProcessor(DataProcessor):
    def __init__(self, database_connection):
        self._db_conn = database_connection #encapsulated attribute

    def process_data(self):
        print("Querying database...")  # Concrete method (with implementation)
        try:
            # Simulate database query and processing
            cursor = self._db_conn.cursor()
            cursor.execute("SELECT data FROM my_table")
            data = cursor.fetchall()
            # Simulate data processing
            processed_data = [row[0].upper() for row in data]
            return processed_data
        except Exception as e:
            return f"Database error: {e}"

# Example Usage

# CSV Example
csv_processor = CSVProcessor("my_data.csv") #assume this file exists
# csv_result = csv_processor.process_data()
# print("CSV Processed Data:", csv_result)

# Database Example (replace with actual database connection)
class MockDatabaseConnection: #mock class for demonstration
    def cursor(self):
        return MockCursor()

class MockCursor:
    def execute(self, query):
        pass
    def fetchall(self):
        return [("data1",), ("data2",), ("data3",)]

mock_db_conn = MockDatabaseConnection()

db_processor = DatabaseProcessor(mock_db_conn)
# db_result = db_processor.process_data()
# print("Database Processed Data:", db_result)

# Abstraction in Action:
def analyze_data(processor: DataProcessor): #type hinting showing the interface.
    print("Starting data analysis...")
    return processor.process_data()

# We can pass either a CSVProcessor or DatabaseProcessor to analyze_data
print("Analysis of CSV:", analyze_data(csv_processor))
print("Analysis of Database:", analyze_data(db_processor))