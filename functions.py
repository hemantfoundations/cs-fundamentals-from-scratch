# functions.py
# This file introduces basic functions in Python.

def add(a, b):
    return a + b

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Function calls
result = add(3, 4)
print("Addition result:", result)

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))
