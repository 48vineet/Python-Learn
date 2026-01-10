
#! CHAPTER 5 – DICTIONARY & SETS

# dictionary is the collection of key value pairs
# * a =  {
# *        "key": "value",
# *        "harry": "code",
# *        "marks": "100",
# *        "list": [1, 2, 9]
# *     }
# print(a["key"])  # Output: "value"
# print(a["list"])  # Output: [1, 2, 9]

# * PROPERTIES OF PYTHON DICTIONARIES
# ? 1. It is unordered.
# ? 2. It is mutable.
# ? 3. It is indexed.
# ? 4. Cannot contain duplicate keys.


# * Methods
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

# * SETS IN PYTHON.
# ? Set is a collection of non-repetitive elements.
# s = set()
# no repetition allowed!
# s.add(1)
# s.add(2)
# or set ={1,2}

# * PROPERTIES OF SETS
# 1. Sets are unordered = > Element’s order doesn’t matter
# 2. Sets are unindexed = > Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

# Method                     Shortcut    Description
# add()                      -           Adds an element to the set

# clear()                    -           Removes all the elements from the set

# copy()                     -           Returns a copy of the set

# difference()               -           Returns a set containing the difference between two or more sets

# difference_update()        -=          Removes the items in this set that are also included in another, specified set

# discard()                  -           Removes the specified item

# intersection()             &           Returns a set, that is the intersection of two other sets

# intersection_update()      &=          Removes the items in this set that are not present in other, specified set(s)

# isdisjoint()               -           Returns whether two sets have an intersection or not

# issubset()                 <=          Returns True if all items of this set are present in another set

# <                          <           Returns True if all items of this set are present in another, larger set

# issuperset()               >=          Returns True if all items of another set are present in this set

# >                          >           Returns True if all items of another, smaller set are present in this set

# pop()                      -           Removes an element from the set

# remove()                   -           Removes the specified element

# symmetric_difference()     ^           Returns a set with the symmetric differences of two sets

# symmetric_difference_update() ^=       Inserts the symmetric differences from this set and another

# union()                    |           Returns a set containing the union of sets

# update()                   |=          Updates the set with the union of this set and others


#! CHAPTER 5 – PRACTICE SET

# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
# 2. Write a program to input eight numbers from the user and display all the unique
# numbers(once).
# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')  # length of s after these operations?
# 5. s = {}
# What is the type of 's'?
# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
# 7. If the names of 2 friends are same
# what will happen to the program in problem
# 6?
# 8. If languages of two friends are same
# what will happen to the program in problem
# 6?
# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1, 2]}


# name = {
#     "p1": {
#         "we": "ham",
#         "you": "app",
#         "they": "wo"
#     },
#     "p2": {
#         "I": "main",
#         "boy": "ladka",
#         "girl": "ladki"
#     }
# }

# s = set()

# for i in range(0, 9):
#     num = int(input("Enter the no upto 8 : "))
#     s.add(num)

# print(s)


# s = {
#     18: "18"
# }

# print(s)

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')

# ss = len(s)
# print(ss)

lang = {}

for i in range(0, 5):
    key = input("Enter the your name : ")
    val = input("Enther your fac language : ")
    lang.update({key: val})

print(lang)
