# Python Variables & Comments 

------------------------------------------------------------------------

## Definition

A variable is a named memory location that stores data.\
Python variables do NOT need type declaration.\
The data type is decided at runtime.

------------------------------------------------------------------------

## Basic Variable Assignment

``` python
x = 10
name = "Satyendra"
price = 99.99
is_active = True

print(x)
print(name)
print(price)
print(is_active)
```

------------------------------------------------------------------------

## Checking Data Type of Variables

``` python
print(type(x))
print(type(name))
print(type(price))
print(type(is_active))
```

------------------------------------------------------------------------

## Type Casting During Declaration

``` python
age = int(25)
```

------------------------------------------------------------------------

## Type Casting (Conversion)

``` python
num_str = "100"
num_int = int(num_str)
```

------------------------------------------------------------------------

## Python is Dynamically Typed

``` python
value = 100
print(value, type(value))

value = "One Hundred"
print(value, type(value))
```

------------------------------------------------------------------------

## Variable Naming Rules

1.  Must start with a letter or underscore\
2.  Cannot start with a number\
3.  Can contain letters, numbers, underscore\
4.  Case-sensitive\
5.  Cannot use keywords

### Valid Variable Names

``` python
user_name = "Ram"
_age = 25
totalMarks = 450

print(user_name, _age, totalMarks)
```

### Invalid Variable Names (Do Not Run)

``` python
# 1name = "error"
# total-marks = 500
# class = "python"
```

------------------------------------------------------------------------

## Multiple Assignment

``` python
a, b, c = 1, 2, 3
print(a, b, c)
```

### Same Value to Multiple Variables

``` python
x = y = z = 50
print(x, y, z)
```

------------------------------------------------------------------------

## Variable Swapping (Without Temp Variable)

``` python
p = 5
q = 10

p, q = q, p
print("p:", p)
print("q:", q)
```

------------------------------------------------------------------------

## Variable Scope (Basic Idea)

``` python
num = 20  # global variable

def test():
    num = 10  # local variable
    print("Inside function:", num)

test()
print("Outside function:", num)
```

------------------------------------------------------------------------

##  Questions

**Q1: What is a variable?**\
A variable is used to store data in memory.

**Q2: Does Python need variable type declaration?**\
No. Python is dynamically typed.

**Q3: Can a variable change its data type?**\
Yes.

**Q4: Are Python variables case-sensitive?**\
Yes. `age` and `Age` are different.

**Q5: What happens if we use a keyword as a variable?**\
SyntaxError occurs.

------------------------------------------------------------------------

# Comments in Python

A comment is a piece of text in a program that is not executed by the
interpreter.\
Comments are used to explain the code and make it more readable.

### Single Line Comment

``` python
# This is a comment
print("Om Shri Ganeshaya Namah")
```

------------------------------------------------------------------------

## Multi-line Comment Using Triple Quotes

``` python
'''
This is a multi line comment
This is the second line of the comment
This is the third line of the comment
'''
```

OR

``` python
\"\"\"
This is a multi line comment
This is the second line of the comment
This is the third line of the comment
\"\"\"
```

⚠ Note: Python does not officially support multi-line comments.\
Triple quotes create multi-line strings, not true comments.

### Proof

``` python
a = '''This is a multi line string
This is the second line of the string
This is the third line of the string'''
print(a)
```

------------------------------------------------------------------------

## Best Practice for Multi-line Comment

``` python
# This is a multi line comment
# This is the second line of the comment
# This is the third line of the comment
```

------------------------------------------------------------------------

``` python
print("End of the program")
print("Namste!!")
```

------------------------------------------------------------------------

**End of Notes**
