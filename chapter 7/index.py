# CHAPTER 7 – LOOPS IN PYTHON

# * WHILE LOOP
# ? Syntax:
# while (condition):  # The block keeps executing until the condition is true
#     # Body of the loop


# ? Example:
# i = 0
# while i < 5:  # print "Harry" – 5 times!
#     print("Harry")
#     i = i + 1

# * FOR LOOP
# A for loop is used to iterate through a sequence like list, tuple, or string[iterables]
# * Syntax:
# l = [1, 7, 8]
# for item in l:
#   print(item)  # prints 1, 7 and 8

# * RANGE FUNCTION IN PYTHON
# ? The range() function in python is used to generate a sequence of number.
# ? We can also specify the start, stop and step-size as follows:
# * range(start, stop, step_size)
# ? step_size is usually not used with range()
# ? AN EXAMPLE DEMONSTRATING RANGE() FUNCTION.
# * for i in range(0, 7):  # range(7) can also be used.
#      print(i)  # prints 0 to 6

# * FOR LOOP WITH ELSE
# * An optional else can be used with a for loop if the code is to be executed when the
# *loops exhausts.
# ?Example:
# l = [1, 7, 8]
# for item in l:
#   print(item)
# else:
#   print("done")  # this is printed when the loop exhausts!

# ? Output:
# ? 1
# ? 7
# ? 8
# ? done

#! CHAPTER 7 – PRACTICE SET
# 1. Write a program to print multiplication table of a given number using for loop.
# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# 3. Attempt problem 1 using while loop.
# 4. Write a program to find whether a given number is prime or not .
# 5. Write a program to find the sum of first n natural numbers using while loop.
# 6. Write a program to calculate the factorial of a given number using for loop.
# 7. Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3
# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3
# 9. Write a program to print the following star pattern.
# * * *
# * * for n = 3
# * * *
# 10. Write a program to print multiplication table of n using for loops in reversed
# order.


# for i in range(1, 11):
#     print(f" 5 x {i} = {5 * i}")

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if "S" in name[0]:
#         print(f"Welcome {name}")


# i = 0
# while i < 6:
#     print(i)
#     i += 1


# num = int(input("Enter the number: "))
# isPrime = False

# for i in range(0, num):
#     if (num % 2 != 0):
#         isPrime = True
#     else:
#         isPrime = False

# print(isPrime)
