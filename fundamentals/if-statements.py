temperature = 3

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")


# elif

score = 100

if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
elif score >= 70:
    print("You got a C")
elif score >= 60:
    print("You got a D")
else:
    print("You got an F")   

# free memory server use case

free_memory_gb = 2

if free_memory_gb >= 4:
    print("You have enough memory to run the application")
else:
    print("You do not have enough memory to run the application")


# Exercise

age = 17

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


cpu_usage = 8

if cpu_usage >= 6:
    print("The server is under heavy load")
elif cpu_usage >= 4:
    print("The server is under moderate load")
else:
    print("The server is under light load")