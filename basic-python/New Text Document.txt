# variable
x = 10
name = "Jahed"
is_active = True
# Python Data Types


# 1. Integers

x = 10
y = -5



# 2. Floats

pi = 3.14
temperature = -5.6

# 3. Strings

name = "Jahed"
greeting = 'Hello, world!'


# 4. Booleans

is_active = True
is_finished = False


# 5. Lists

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]


# 6. Dictionaries

student = {"name": "Jahed", "age": 22}
person = {"first_name": "John", "last_name": "Doe"}

# 7. Tuples

coordinates = (10, 20)
dimensions = (5, 10, 15)

# 8. Sets

colors = {"red", "green", "blue"}
numbers = {1, 2, 3, 4}


# 9. None
value = None



# Python Data Types: List, Tuple, Set, Dictionary

# List

greet = ["Hello", "World", "Bangladesh"]
greet[1] = "BD"  # change value
print(greet)  # ['Hello', 'BD', 'Bangladesh']

## Tuple

coordinates = (10, 20)
print(coordinates[0])  # 10

## Set
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.remove("green")
print(colors)

## Dictionary
person = {"name": "Jahed", "age": 25}
print(person["name"])  # Jahed

## List Comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

## Dictionary Manipulation

#  Access Values
person = {"name": "Jahed", "age": 25}
print(person["name"])  # Jahed

#  Add or Update Key-Value
person["email"] = "jahed@example.com"
person["age"] = 26

#  Delete a Key
del person["age"]

# Loop through Dictionary
for key, value in person.items():
    print(key, ":", value)
