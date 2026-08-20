count = 10

while count > 0:
    print(count)
    count = count - 1
print("Go!")

max_attempts = 5
attempt = 0
connected = False

while attempt < max_attempts and not connected:
    attempt += 1
    print(f"Attempt {attempt}...")
    if attempt == 3:
        connected = True
        print("Connected!")


# Exercise 

number = 10

while number > 0:
    print(number)
    number -= 1


total = 0
count = 1

while count <= 5:
    total += count
    count += 1
print(total)
