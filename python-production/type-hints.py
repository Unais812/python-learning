# provide labels as to what the values should be making code easier to read and catch errors

def add(a: int, b: int):
    return a + b

print(add(10, 43))


def clean_username(name: str):
    return name.strip().lower()

def average(numbers: list[float]):
    return sum(numbers) / len(numbers)

print(clean_username(" Unais   "))
print(average([10.8, 34.0, 43.5, 89.4]))


# Exercise


def square(num: int):
    return num ** 2
print(square(5))

def greet(name: str, greeting: str) -> str:
    return f"{greeting}, {name}"
print(greet("unais", "Hello"))

def total(numbers: list[int]):
    return sum(numbers)

numbers = [50, 70, 32, 12]
print(total(numbers))

def is_adult(age: int) -> bool:
    if age > 25:
        return True
    else:
        return False
print(is_adult(3))