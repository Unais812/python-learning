fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(len(fruits))
fruits.append("pear")
print(fruits)

###########################

failed_servers = []

failed_servers.append("web-03")
failed_servers.append("db-01")

print(f"{len(failed_servers)} servers failed")
print(failed_servers)

###########################

colours = ["red", "blue", "green"]
print(colours[0])
print(colours[2])
colours.append("yellow")
print(colours)

numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)
print(sum(numbers))
