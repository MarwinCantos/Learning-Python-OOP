class Info:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

user1 = Info("Alice", 30)
user2 = Info("Bob", 25)
user3= Info("Charlie", 25)
user4 = Info("David", 30)


print(f"My Name is {user1.name} and I am {user1.age} years old.")
print(f"My Name is {user2.name} and I am {user2.age} years old.")
print(f"My Name is {user3.name} and I am {user3.age} years old.")
print(f"My Name is {user4.name} and I am {user4.age} years old.")

