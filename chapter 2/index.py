
# * Primarily these are the following data types in Python:
# ? 1. Integers
# ? 2. Floating point numbers
# ? 3. Strings
# ? 4. Booleans
# ? 5. None

# *a = 71  # identifies a as class <int>
# *b = 88.44  # identifies b as class <float>
# *name = "harry"  # identifies name as class <str>

# * Following are some common operators in python:
# ? 1. Arithmetic operators: +, -, *, / etc.
# ? 2. Assignment operators:  =, +=, -= etc.
# ? 3. Assignment operators:  =, +=, -= etc.
# ? 4. Logical operators: and, or, not.

# * a = 31
# * type(a)  # class <int>

# ? str(31) = > "31"   # integer to string conversion
# ? int("32") = > 32  # string to integer conversion
# ? float(32) = > 32.0  # integer to float conversion

#! Practice Questions

# ? 1. Write a python program to add two numbers.
# ? 2. Write a python program to find remainder when a number is divided by z.
# ? 3. Check the type of variable assigned using input() function.
# ? 4. Use comparison operator to find out whether ‘a’ given variable a is greater than
# ?     ‘b’ or not . Take a = 34 and b = 80
# ? 5. Write a python program to find an average of two numbers entered by the user.
# ? 6. Write a python program to calculate the square of a number entered by the user.

a = 10
b = 20
print(a + b)


def rem(a, b):
    return a % b


print(rem(10, 20))

answer = input("Checking type of input : ")
print(type(answer))

v = 34
m = 80

print(v > m)


inp1 = int(input('Enter the Input 1 : '))
inp2 = int(input("Enter input 2 : "))

avg = (inp1 + inp2) / 2
print(avg)

square = int(input('Enter the Input 1 to find square: '))

print(pow(square, 2))
