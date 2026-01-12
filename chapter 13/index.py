
#! CHAPTER 13 – ADVANCED PYTHON 2

# VIRTUAL ENVIRIONMENT
# An environment which is same as the system interpreter but is isolated from the other
# Python environments on the system.
# INSTALLATION
# To use virtual environments, we write:
# pip install virtualenv  # Install the package
# We create a new environment using:
# virtualenv myprojectenv  # Creates a new venv
# The next step after creating the virtual environment is to activate it.
# We can now use this virtual environment as a separate Python installation.

#! PIP FREEZE COMMAND
# ‘pip freeze’ returns all the package installed in a given python environment along with
# the versions. matlab jo jo installed hai vo dikhata

#! LAMBDA FUNCTIONS
# Function created using an expression using ‘lambda’ keyword.
# Syntax:
# lambda arguments:expressions
# # can be used as a normal function

#? square = lambda x:x*x
#? square(6)  # returns 36
#? sum = lambda a,b,c:a+b+c
#? sum(1,2,3) # returns 6

# JOIN METHOD (STRINGS)
# Creates a string from iterable objects.
# l = ["apple", "mango", "banana"]
# result = ", and, ".join(l)
# print(result)
# The above line will return “apple,and,mango,and,banana”.

#! Map Example

square = lambda x : x*x
num1 = [10,20,30]

ans = map(square, num1)
print(list(ans))

#! Filter Example

# Define a function to filter even numbers
is_even = lambda x: x % 2 == 0
num2 = [10, 15, 20, 25, 30]

# Apply the filter function
filtered = filter(is_even, num2)
print(list(filtered))  # Output: [10, 20, 30]
