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
Day 03 - Loops

Goal:
Understand how loops automate repetitive tasks.
Loops are heavily used while processing datasets.

Author: Raksha Singh
Project: RepSpeed AI Workout Recognition
"""

# Loop through a list
workout = [10, 12, 15, 11, 14]

for reps in workout:
    print(f"Workout completed: {reps} reps")

print()

# range()
print("Using range():")

for i in range(5):
    print(i)

print()

# range(start, stop, step)

for i in range(2, 10, 2):
    print(i)

print()

# Loop through names

names = ["Raksha", "Riri", "Python"]

for name in names:
    print(name.upper())

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


"""
Day 05 - Decision Making (if, elif, else)

Goal:
Learn how Python makes decisions based on conditions.

Author: Raksha Singh
Project: RepSpeed AI Workout Recognition
"""

# Basic if

age = 21

if age >= 18:
    print("Adult")

# if-else

marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# if-elif-else

score = 82

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Needs Improvement")

# AI Example

confidence = 91

if confidence >= 90:
    print("Prediction Accepted")
else:
    print("Prediction Rejected")

"""
Day 06 - Tuples

Author: Raksha Singh
Project: RepSpeed AI Workout Recognition

Goal:
Learn immutable data structures in Python.
"""

# Creating Tuples

student = ("Raksha", 21, "Somaiya")

print(student)

# Accessing Values

print(student[0])

print(student[-1])

# Slicing

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

# count()

numbers = (10, 20, 20, 30)

print(numbers.count(20))

# index()

print(numbers.index(30))

# Tuples are immutable

# numbers[0] = 100   # Uncomment to see the TypeError

"""
=========================================
Day 07 - Python Core Revision

Author: Raksha Singh
Project: RepSpeed AI Workout Recognition

Goal:
Revise all Python concepts learned before
starting NumPy.
=========================================
"""

print("\n========== PYTHON CORE COMPLETED ==========\n")

# Variables

name = "Raksha"
role = "Future Data Scientist"

print(name)
print(role)

# String

language = "Python"

print(language.upper())
print(language[:3])

# List

skills = ["Python", "SQL"]

skills.append("NumPy")

print(skills)

# Dictionary

student = {
    "name": "Raksha",
    "age": 21,
    "college": "Somaiya"
}

print(student["college"])

# Tuple

coordinates = (19.0760, 72.8777)

print(coordinates)

# Set

unique_numbers = {1,2,2,3,4,4}

print(unique_numbers)

# Function

def square(number):
    return number * number

print(square(5))

# Loop

for skill in skills:
    print(skill)

# Decision Making

accuracy = 94

if accuracy >= 90:
    print("Excellent Model")
else:
    print("Needs Improvement")

# Exception Handling

try:
    number = int("hello")
except ValueError:
    print("ValueError handled successfully")

# File Handling

with open("sample.txt", "w") as file:
    file.write("Python Revision Completed")

print("\nPython Core Successfully Completed!")
print("Next Topic -> NumPy")
