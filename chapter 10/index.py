# CHAPTER 10 - OBJECT ORIENTED PROGRAMMING

# Solving a problem by creating object is one of the most popular approaches in
# programming. This is called object-oriented programming.
# This concept focuses on using reusable code(DRY Principle).

class Employee:
    name = "Vineet"
    age = 19
    dob = "02/02/2006"


vineet = Employee()
print(vineet.age)

vineet.age = 20
vineet.work = "google"
print(vineet.age)
print(vineet.work)

# * OBJECT
# An object is an instantiation of a class . When class is defined, a template(info) is
# defined. Memory is allocated only after object instantiation.
# Objects of a given class can invoke the methods available to it without revealing the
# implementation details to the user. – Abstractions & Encapsulation!
