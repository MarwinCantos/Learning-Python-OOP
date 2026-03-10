class Info:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

user1 = Info("Alice", 30)

print(f"My Name is {user1.name} and I am {user1.age} years old.")


