# Basic Python Code Examples

## 1. Hello World
```python
print("Hello, World!")
```

## 2. Variables and Data Types
```python
name = "Alice"
age = 25
height = 5.6
is_student = True
print(name, age, height, is_student)
```

## 3. Conditional Statements
```python
num = 10
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
```

## 4. Loops
### For Loop
```python
for i in range(5):
    print("Iteration", i)
```

### While Loop
```python
count = 0
while count < 5:
    print("Count is", count)
    count += 1
```

## 5. Functions
```python
def greet(name):
    return "Hello, " + name

print(greet("Alice"))
```

## 6. Lists
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
```

## 7. Dictionaries
```python
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"])
```

## 8. Classes and Objects
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

p = Person("Alice", 25)
print(p.greet())
```

## 9. File Handling
```python
with open("sample.txt", "w") as file:
    file.write("Hello, World!")
```

## 10. Exception Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")