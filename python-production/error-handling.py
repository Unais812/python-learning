# crashes program: result = 10 / 0 

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by 0")
    result = 0
print(result)

def parse_age(text):
    try:
        return int(text)
    except ValueError:
        print(f"'{text}' is not a valid number")
        return None

print(parse_age(29))
print(parse_age("hello"))\


# Exercise 


def safe_divide(num, num2):
    try:
         result = num / num2
         return(result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
print(safe_divide(20, 0))


def to_number(string):
    try:
        return int(string)
    except ValueError:
        return(f"The value '{string}' is not a valid number")

print(to_number("9839"))

def get_age(age):
    if age < 0:
        return ValueError("Age cannot be negative")
    else:
        return(f"Age selected as '{age}'")
print(get_age(-78))