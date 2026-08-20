person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
}

print(person["name"])
print(person["age"])
print(person["city"])
person["age"] = 31
person["job"] = "DevOps Engineer"
print(person)

server = {
    "name": "web-01",
    "cpu_cores": 8,
    "memory_gb": 32,
    "is_online": True
}

print(f"{server['name']} has {server['cpu_cores']} cpu cores and {server['memory_gb']} GB of memory Online status: {server['is_online']}")

book = {
    "title": "DevOps book",
    "author": "Unais",
    "year": 2026,
}

print(book["title"])
print(book["author"])
book["year"] = 2024
book["pages"] = 482
print(book)