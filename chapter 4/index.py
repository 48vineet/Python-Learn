
#! CHAPTER 4 – LISTS AND TUPLES

# * Python lists are containers to store a set of values of any data type. also it is mutable

List = ["Vineet", 19, "Welcome", "Coding DSA"]

# ? list[0]     -> Vineet
# ? List[0:2]   -> [ Vineet , 19]

# List[0] = "Vineet Mali"
# print(List)

# * Methods in List

# ? append()	Adds an element at the end of the list

# ? clear()	Removes all the elements from the list

# ? copy()	Returns a copy of the list

# ? count()	Returns the number of elements with the specified value

# ? extend()	Add the elements of a list ( or any iterable), to the end of the current list

# ? index()	Returns the index of the first element with the specified value

# ? insert()	Adds an element at the specified position

# ? pop()	Removes the element at the specified position

# ? remove()	Removes the item with the specified value

# ? reverse()	Reverses the order of the list

# ? sort()	Sorts the list

# * TUPLES IN PYTHON
# * A tuple is an immutable data type in python.

mytuple = ("apple", "banana", "cherry")

a = (1, 7, 2)

# * a.count(1): a count(1) will return number of times 1 occurs in a.
# * a.index(1) will return the index of first occurrence of 1 in a.

#! CHAPTER 4 - PRACTICE SET
# ? 1. Write a program to store seven fruits in a list entered by the user.
# ? 2. Write a program to accept marks of 6 students and display them in a sorted
# ?    manner.
# ? 3. Check that a tuple type cannot be changed in python.
# ? 4. Write a program to sum a list with 4 numbers.
# ? 5. Write a program to count the number of zeros in the following tuple:
# ? a = (7, 0, 8, 0, 0, 9)

# l1 = []
# no = int(input("Enter the No Of Fruits : "))
# for i in range(1, no):
#     fruit = input(f"Enter the Fruit {i} : ")
#     l1.append(fruit)
# print(l1)

# l2 = []
# no = int(input("Enter the No Of Student : "))
# for i in range(1, no):
#     student = int(input(f"Enter the Student Marks {i} : "))
#     l2.append(student)
# l2.sort()
# print(l2)


# tuple = (10, 12, 12, 32, 12)
# tuple[0] = 13
# print(tuple)

# a = [7, 8, 0, 9]
# sum = 0
# for i in range(0, len(a)):
#     sum = sum + a[i]
# print(sum)

# a = (7, 0, 8, 0, 0, 9, 0)
# ans = a.count(0)
# print(ans)
