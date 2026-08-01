# Day 01 - Python Basics
# Goal: Learn Python fundamentals before working with datasets

name = "Raksha"
age = 20

print(name)
print(age)

print(type(name))
print(type(age))

"""
Day 02 - Python Lists

Goal:
Learn how to create, modify and access lists.
Lists are one of the most important data structures in Python and are
used extensively in Data Science and Machine Learning.

Author: Raksha Singh
Project: RepSpeed AI Workout Recognition
"""

# Creating a list
numbers = [10, 20, 30]

print("Original List:", numbers)

# Accessing elements
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Adding elements
numbers.append(40)
print("After append():", numbers)

numbers.insert(1, 99)
print("After insert():", numbers)

# Removing elements
numbers.pop()
print("After pop():", numbers)

numbers.remove(99)
print("After remove():", numbers)

# Length
print("Length:", len(numbers))

# Membership
print(20 in numbers)

# Slicing
print(numbers[0:2])

# Sorting
marks = [88, 75, 95, 61]
marks.sort()
print("Sorted:", marks)

marks.reverse()
print("Reverse:", marks)

"""
Day 04 - Functions

Goal:
Understand why functions exist, how to create them,
how parameters work, and the difference between
print() and return().

Author: Raksha Singh
Project: RepSpeed AI Workout Recognition
"""

# Function with no parameters
def greet():
    print("Welcome to the RepSpeed AI Project!")

# Function with one parameter
def greet_user(name):
    print(f"Hello, {name}!")

# Function with two parameters
def add(a, b):
    return a + b


# Testing the functions
greet()
greet_user("Raksha")

result = add(5, 7)
print(f"Addition Result: {result}")
