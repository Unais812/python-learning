# for each item in the list called fruits, we are naming that item fruit, and for every fruit in fruits, do the thing below. 
# The loop takes the first item, calls it fruit, runs the indented line. 
# Then it takes the second item, calls it fruit, runs the line again. 
# Then the third. Then it stops, because there are no more items.

fruits = ["apple", "banana", "orange"]

for random in fruits:
    print(random)

# Often you want to loop a set number of times rather than over a list.
# range() gives you a sequence of numbers to loop over:

for i in range(5):
    print(i)

# Adding up size of a list of files

file_size_mb = [12, 8, 36, 23]

total = 0
for size in file_size_mb:
    total = total + size 
print(f"Total size: {total} MB")


# Exercise 

animals = ["cat", "dog", "rabbit", "girrafe", "elephant"]

for animal in animals:
    print(animal)

for i in range(5):
    print(i)

price = [10, 20, 30, 40, 50]
total = 0

for cost in price:
    total = total + cost
print(f"Total price: £{total}")

for animal in animals:
    print(animal.upper())
 