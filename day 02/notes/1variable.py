
# -----------------------------------------------------
# DEFINITION:
# A variable is a named memory location that stores data.
# Python variables do NOT need type declaration.
# The data type is decided at runtime.
# -----------------------------------------------------


# -----------------------------------------------------
# BASIC VARIABLE ASSIGNMENT
# -----------------------------------------------------
x = 10
name = "Satyendra"
price = 99.99
is_active = True

print(x)
print(name)
print(price)
print(is_active)


# -----------------------------------------------------
# CHECKING DATA TYPE OF VARIABLES
# -----------------------------------------------------
print(type(x))
print(type(name))
print(type(price))
print(type(is_active))


# -----------------------------------------------------
#TYPE CASTING DURING DECLARATION
age = int(25)  # age is an integer

# -----------------------------------------------------
# TYPE CASTING (CONVERSION)
num_str = "100"
num_int = int(num_str)  # Convert string to integer


# -----------------------------------------------------
# PYTHON IS DYNAMICALLY TYPED
# Same variable can store different data types
# -----------------------------------------------------
value = 100
print(value, type(value))

value = "One Hundred"
print(value, type(value))


# -----------------------------------------------------
# VARIABLE NAMING RULES (IMPORTANT)
# -----------------------------------------------------
# 1. Must start with a letter or underscore
# 2. Cannot start with a number
# 3. Can contain letters, numbers, underscore
# 4. Case-sensitive
# 5. Cannot use keywords


# VALID VARIABLE NAMES
user_name = "Ram"
_age = 25
totalMarks = 450

print(user_name, _age, totalMarks)


# INVALID VARIABLE NAMES (DO NOT RUN)
# 1name = "error"
# total-marks = 500
# class = "python"


# -----------------------------------------------------
# MULTIPLE ASSIGNMENT
# -----------------------------------------------------
a, b, c = 1, 2, 3
print(a, b, c)


# SAME VALUE TO MULTIPLE VARIABLES
x = y = z = 50
print(x, y, z)


# -----------------------------------------------------
# VARIABLE SWAPPING (WITHOUT TEMP VARIABLE)
# -----------------------------------------------------
p = 5
q = 10

p, q = q, p
print("p:", p)
print("q:", q)


# -----------------------------------------------------
# VARIABLE SCOPE (BASIC IDEA)
# -----------------------------------------------------
# Variable created inside a function is local
# Variable created outside is global

num = 20  # global variable

def test():
    num = 10  # local variable
    print("Inside function:", num)

test()
print("Outside function:", num)


# -----------------------------------------------------
# QUESTION & ANSWER SECTION (INTERVIEW STYLE)
# -----------------------------------------------------

# Q1: What is a variable?
# A: A variable is used to store data in memory.

# Q2: Does Python need variable type declaration?
# A: No. Python is dynamically typed.

# Q3: Can a variable change its data type?
# A: Yes.

# Q4: Are Python variables case-sensitive?
# A: Yes. age and Age are different.

# Q5: What happens if we use a keyword as a variable?
# A: SyntaxError occurs.


# -----------------------------------------------------
# PROGRAM END
# -----------------------------------------------------
