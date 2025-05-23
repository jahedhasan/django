# Python Data Types

Python has several built-in data types, which are used to store values. Below are the common data types in Python:

## 1. Integers
Integers are whole numbers, positive or negative, without a decimal point.

```python
x = 10
y = -5
```


## 2. Floats
Floats are numbers with a decimal point.

```python
pi = 3.14
temperature = -5.6
```

## 3. Strings
Strings are sequences of characters enclosed in quotes (single or double).

```python
name = "Jahed"
greeting = 'Hello, world!'
```

4. Booleans
Booleans represent either True or False.

```python
is_active = True
is_finished = False
```

## 5. Lists
Lists are ordered collections of items, which can be of different types.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
```

## 6. Dictionaries
Dictionaries are unordered collections of key-value pairs.

```python
student = {"name": "Jahed", "age": 22}
person = {"first_name": "John", "last_name": "Doe"}
```
## 7. Tuples
Tuples are similar to lists but are immutable (cannot be modified after creation).

```python
coordinates = (10, 20)
dimensions = (5, 10, 15)
```
## 8. Sets
Sets are unordered collections of unique elements.

```python
colors = {"red", "green", "blue"}
numbers = {1, 2, 3, 4}
```

## 9. None
None is a special data type used to represent the absence of a value or a null value.

```python
value = None
```


# Python Loops and Functions

## Loops
Loops are used to repeat a block of code multiple times.

### 1. While Loop
Executes a block of code as long as a condition is true.

```python
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

```
### 2. For Loop
Used for iterating over a sequence (like a list, tuple, string, or range).

```python
for i in range(5):
    print("Number:", i)
```
# Functions
Functions are blocks of reusable code that perform a specific task.

## 1. Defining a Function
```python
def greet():
    print("Hello, world!")
```
## 2. Calling a Function
```python
greet()
```
## 3. Function with Parameters
```python
def greet(name):
    print("Hello,", name)

greet("Jahed")
```
## 4. Function with Return Value
```python

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)
```
## 5. Default Parameters
```python

def greet(name="Guest"):
    print("Hello,", name)

greet()           # Hello, Guest
greet("Jahed")    # Hello, Jahed

```


# Python Data Types: List, Tuple, Set, Dictionary

## List
- Ordered
- Mutable (can change items)
- Allows duplicate values

### Code Example
```python
greet = ["Hello", "World", "Bangladesh"]
greet[1] = "BD"  # change value
print(greet)  # ['Hello', 'BD', 'Bangladesh']
```

## Tuple
- Ordered  
- Immutable (cannot change items)  
- Allows duplicate values  

### Code Example
```python
coordinates = (10, 20)
print(coordinates[0])  # 10
```
## Set
- Unordered  
- No duplicate values  
- Mutable (can add/remove items, but items themselves must be immutable)  

### Code Example
```python
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.remove("green")
print(colors)
```

## Dictionary
- Unordered (Python 3.7+ maintains insertion order)  
- Stores data in **key-value** pairs  
- Keys must be unique and immutable  

### Code Example
```python
person = {"name": "Jahed", "age": 25}
print(person["name"])  # Jahed
```## List Comprehension

List comprehension is a concise way to create lists.

### Example: Create a list of squares from 1 to 5
```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

## Dictionary Manipulation

### 1. Access Values
#### Example:
```python
person = {"name": "Jahed", "age": 25}
print(person["name"])  # Jahed
```
