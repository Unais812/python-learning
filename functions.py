def add(a, b):
    return a + b

result = add(5, 10)
print(result)

# Now a small realistic use. A function that cleans up a username, wrapping the logic from the strings lesson so we can reuse it.

def clean_username(name):
    return name.strip().lower()

print(clean_username("  Unais Rashid "))
print(clean_username("  BOb"))

# You can also give arguments default values, used when the caller does not supply one:

def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

print(greet("Unais"))
print(greet("unais", "hi"))

# Exercise

def square(num):
    return num ** 2

print(square(10))

def is_even(num):
    return num % 2 == 0

print(is_even(10))

def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

print(average([10, 40, 30]))

def greet_user(name, greeting="Hi"):
    return f"{greeting} {name}"

print(greet_user("unais"))