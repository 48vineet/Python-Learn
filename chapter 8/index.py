# CHAPTER 8 – FUNCTIONS & RECURSIONS

# * A function is a group of statements performing a specific task.

# def func1():
#     print('hello')

# ? DEFAULT PARAMETER VALUE
# We can have a value as default as default argument in a function.
# If we specify name = “stranger” in the line containing def , this value is used when no
# argument is passed.
# Example:

# def greet(name="stranger"):
#     # function body
# greet()  # name will be "stranger" in function body (default)
# greet("harry")  # name will be "harry" in function body (passed)

# ! RECURSION
# * Recursion is a function which calls itself.
# * It is used to directly use a mathematical formula as function.
# Example:
# factorial(n) = n x factorial(n-1)
# This function can be defined as follows:
# def factorial(n):
#   if i == 0 or i == 1:  # base condition which doesn’t call the function
#  any further
#   return 1
# else:
#   return n*factorial(n-1)  # function calling itself


#! CHAPTER 8 – PRACTICE SET
# 1. Write a program using functions to find greatest of three numbers.
# 2. Write a python program using function to convert Celsius to Fahrenheit.
# 3. How do you prevent a python print() function to print a new line at the end.
# 4. Write a recursive function to calculate the sum of first n natural numbers.
# 5. Write a python function to print first n lines of the following pattern:
# ***
# **
# * - for n = 3
# 6. Write a python function which converts inches to cms.
# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.
# 8. Write a python function to print multiplication table of a given number.

# def gre(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         print(num1)
#     elif num2 > num1 and num2 > num3:
#         print(num2)
#     elif num3 > num1 and num3 > num2:
#         print(num3)

# gre(10, 50, 30)
