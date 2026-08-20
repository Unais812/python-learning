profile = {
    "name": "Unais",
    "age": 17,
    "city": "Bradford",
}

print(f"Hello my name is {profile['name']}, i am {profile['age']} years old and i live in {profile['city']}")

hobbies = ["football", "basketball", "tennis"]

for hobby in hobbies:
    print(hobby)


# Exercise 2 


numbers = [34, 53, 28, 84, 5, 23, 74, 62, 90, 88, 784, 82, 85]
total = 0
even = 0
odd = 0
for number in numbers:
    total = total + number
    count = (len(numbers))
    average = total / count
print(f"the total is {total}")
print(f"the average is {average}")

for number in numbers:
    if number % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(f"There are {even} even numbers in the list")
print(f"There are {odd} odd numbers in the list")


# Exercise 3 


string = "hello my name is unais and and my name i live in bradford"
words = string.split()
print(words)
print(len(words))

for word in words:
    print(word.upper())

dictionary = {}

for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
print(dictionary)


# Exercise 4 


def grade (score):
    if score >= 90:
        return("You got an A")
    elif score >= 80:
        return("You got a B")
    elif score >= 70:
        return("You got a C")
    elif score >= 60:
        return("You got a D")
    else:
        return("You got an F") 

print(grade(89))


# Exercise 5 


server_1 = {
    "name": "web-01",
    "memory_gb": 3,
    "is_online": True
}

server_2 = {
    "name": "web-02",
    "memory_gb": 7,
    "is_online": False
}

server_3 = {
    "name": "data-01",
    "memory_gb": 10,
    "is_online": True
}

def check_server(server):
    if not server['is_online']:
        return "Warning, server is offline"
    elif server['memory_gb'] < 4:
        return "Low memory"
    else:
        return "Memory is ok"

servers = [server_3, server_1, server_2]
offline = 0
online = 0

for server in servers:
    print(f"Checking sever {server['name']}")
    print(check_server(server))

    if not server['is_online']:
        offline += 1
    else:
        online += 1
print(f"Number of online server: {online}. Number of offline servers: {offline}")