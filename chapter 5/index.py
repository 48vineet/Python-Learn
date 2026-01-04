
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
