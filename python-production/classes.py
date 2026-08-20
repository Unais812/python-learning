# class is blueprint, object is thing made from blueprint
# like a cookie cutter and cookie, cutter is class and cookie is object
# In code, a class defines what data a thing holds and what it can do. An object is one specific instance of that class, with its own values.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# __init__ is a special setup function that runs when you make a new object. 
# It takes the values and stores them on self, which means "this particular object"

    def bark(self):
        return f"{self.name} says woof"

my_dog = Dog("Rex", "Labrador")
print(my_dog.name)
print(my_dog.bark())        


class Server:
    def __init__(self, name, memory_gb):
        self.name = name
        self.memory_gb = memory_gb
        self.is_online = True

    def status_report(self):
        state = "online" if self.is_online else "offline"
        return f"{self.name}: {self.memory_gb} GB, {state}"
    
web = Server("web-01", 32)
db = Server("db-01", 64)

print(web.status_report())
print(db.status_report())


# Exercise 


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self):
        if self.balance > 10:
            withdraw = int(input("How much would you like to withdraw? "))
            self.balance = self.balance - withdraw
            return f"Your current balance is now {self.balance}"
        else: 
            return("Not enough balance to withdraw")

    def show_balance(self):
        return(f"{self.name} balance is currently {self.balance}")

account_1 = BankAccount("Unais", 100000)
account_2 = BankAccount("John", 5)

print(account_1.show_balance())
print(account_1.deposit(6503))
print(account_2.deposit(6000))
print(account_2.withdraw())