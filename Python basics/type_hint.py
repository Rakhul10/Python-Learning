# Type Hints:

# Documentation — Makes code clearer for other programmers
# Error Detection — Tools like mypy can warn about type mismatches
# IDE Support — Better autocomplete and error checking
# Self-Commenting — Shows what types are expected

# Type hints are optional and not enforced at runtime—Python will still run the code even if types don't match. They're mainly for static analysis tools and documentation.
from typing import List, Union

def greet(name: str) -> str:
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    return a + b

# Correct usage:
print(greet("Alice"))           # ✓ OK
print(add_numbers(5, 3))        # ✓ OK

# Type errors (mypy will catch):
print(greet(123))               # ✗ int instead of str
print(add_numbers("5", "3"))    # ✗ str instead of int


##########################use of Union to allow multiple types for a parameter or return value ################################################

def process_list(items: Union[str, List[str]]) ->Union[str, List[str]]:
    return items[::-1]
print(process_list("Hello"))  # Output: 'olleH'
print(process_list([1, 2, 3]))   #expected output is [3, 2, 1] but it will give error as we have defined the type hint as List[str] but we are passing List[int]    
print(process_list(["a", "b", "c"]))  # Output: ['c', 'b', 'a']

############################## CMD to run mypy:#######################################################
# python -m mypy type_hint.py  -> This runs mypy as a Python module

# # Basic check
# mypy test.py

# # Strict mode (most checks)
# mypy --strict test.py

# # Check entire folder
# mypy .

# # Show detailed errors
# mypy --show-error-codes test.py

# # Ignore missing type stubs
# mypy --ignore-missing-imports test.py



##########################################################################################################

################type hint for class ####################################################
class mypython:
    def __init__(self, x: int):
        self.x = x
    def __str__(self) -> str:
        return f"{self.x}"
    
num1 = mypython(10)
num2 = mypython(20)
print (num1 + num2) # unsupported operand type(s) for +: 'mypython' and 'mypython'


###### To fix the above error, we can implement the __add__ method in the mypython class to define how two mypython objects should be added together.
############################## Custom Class with __add__ method #######################################################

class mypython:
    def __init__(self, x: int):
        self.x = x
    
    def __str__(self) -> str:
        return f"{self.x}"
    
    def __add__(self, other: 'mypython') -> 'mypython':
        """Allows adding two mypython objects using the + operator"""
        return mypython(self.x + other.x)

num1 = mypython(10)
num2 = mypython(20)
print(num1 + num2)  # Output: 30