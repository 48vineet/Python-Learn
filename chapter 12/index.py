
#! CHAPTER 12 – ADVANCED PYTHON 1

# * WALRUS OPERATOR
# The walrus operator (:= ), introduced in Python 3.8, allows you to assign values to
# variables as part of an expression. This operator, named for its resemblance to the eyes
# and tusks of a walrus, is officially called the "assignment expression."

# if (n := len([1, 2, 3, 4, 5])) > 3:
#     print(f"List is too long ({n} elements, expected <= 3)")

# ? TYPES DEFINITIONS IN PYTHON

# age: int = 25

# def greeting(name: str) -> str:
#     return f"Hello, {name}!"

# # Usage
# print(greeting("Alice"))  # Output: Hello, Alice!

# ADVANCED TYPE HINTS
# Python's typing module provides more advanced type hints, such as List, Tuple, Dict,
# and Union.

from typing import Dict, List, Tuple, Union

# List of integers
# numbers: List[int] = [1, 2, 3, 4, 5]
# # Tuple of a string and an integer
# person: Tuple[str, int] = ("Alice", 30)
# # Dictionary with string keys and integer values
# scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# # Union type for variables that can hold multiple types
# identifier: Union[int, str] = "ID123"
# identifier = 12345  # Also valid


# MATCH CASE or Switch Statement
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"


# Usage
print(http_status(200))  # Output: OK
print(http_status(404))  # Output: Not Found
print(http_status(500))  # Output: Internal Server Error
print(http_status(403))  # Output: Unknown status


# DICTIONARY MERGE & UPDATE OPERATORS
# New operators | and |= allow for merging and updating dictionaries.
# 49
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# merged = dict1 | dict2
# print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

# You can now use multiple context managers in a single with statement more cleanly
# using the parenthesised context manager
# with (
#     open('file1.txt') as f1,
#     open('file2.txt') as f2
# ):
#     # Process files


#! Try except block
# try:
#     a = int(input("Enter Only Integer: "))
# except Exception as e:
#     print(e)


#! More exception
# try:
#     # Code
# except ZeroDivisionError:
#     # Code
# except TypeError:
#     # Code
# except:
#     # Code
#     # All other exceptions are handled here.

# raise is keyword use to raise the problem if done by devloper like if i performed 1/0 then dividing by zero is not aloowed hence ill code like

# raise ZeroDivisionError("New Error")

# TRY WITH ELSE CLAUSE
# Sometimes we want to run a piece of code when try was successful.
# it runs only when try is suceessfull

# try:
#     # Somecode
# except:
#     # Somecode
# else:
#     # Code
#     # This is executed only if the try was successful


# Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of
# the exception.
# it runs even after the fuinctions returen something means if we want to run finally but before that we have implemenmt ed the reurn statement sp it will noty afrftect that
# try:
#     # Some Code
# except:
#     # Some Code
# finally:
#     # Some Code
#     # Executed regardless of error!


#! ENUMERATE FUNCTION IN PYTHON
# The ‘enumerate’ function adds counter to an iterable and returns it
# for i, item in list1:
# print(i, item)  # Prints the items of list 1 with index
#!LIST COMPREHENSIONS
# List Comprehension is an elegant way to create lists based on existing lists.
# list1 = [1, 7, 12, 11, 22,]
# list2 = [i for item in list 1 if item > 8]
