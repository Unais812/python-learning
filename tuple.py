# tuple is like a list but cannot be changed after creation
# think of it like a reciept, once it is printed you cant edit it, if something is wrong you get a new one

# set is a collection with no duplicates and no order, throws away repeats

# tuple

location = (34.5, 23.4)
print(location[0])
# location[0] = 35.5 this will throw an error because tuples are immutable

# set

tags = {"python", "version", "python"}
print(tags) # will only print python and version, no duplicates


# Finding the unique visitors to a website from a list that has repeats

visits = ["sara", "unny", "tom", "ben", "ben", "sara"]
unique_visits = set(visits)
print(unique_visits) # will only print sara, unny, tom, ben


# Exercise

colours = ("FF0000", "0000FF" "00FF00")
print(colours[0])

words = {"hello", "world", "hello", "python", "test"}
unique_words = set(words)
print(unique_words) # will only print hello, world, python, test
print(len(unique_words)) # will print 4 because there are 4 unique words