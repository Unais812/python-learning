# python has a ton of premade classes already for example lists, sets, variables
# so when i access a dunder method for those e.g. len, it has already been defined behind the scenes
# i am creating a class from scratch so it doesnt have access to these dunder methods by default, i must add them 

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)
    
cart = Cart()
cart.add("apple")
cart.add("bread")

print(len(cart))


# Exercise 


class Playlist:
    def __init__(self):
        self.list = []
    
    def add_song(self, item):
        self.list.append(item)
        return f"{item} has been added to your playlist"

    def __len__(self):
        return len(self.list)
    
    def __str__(self):
        return f"Playlist with {len(self.list)} songs"
    
liked = Playlist()

print(liked.add_song("01"))
print(liked.add_song("02"))
print(len(liked))
print(liked)