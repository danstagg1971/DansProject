class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        if self.breed == "Dog":
            print("bark! bark! bark!")
        if self.breed == "Cat":
            print("meeeeeeooow!")

    def description(self):
        if self.breed == "Dog":
            print(f"This is {self.name}, its a {self.breed} and is {self.age} years old")
        if self.breed == "Cat":
            print(f"This is {self.name}, its a {self.breed} and is {self.age} years old")


dog1 = Dog("Buddy", "Dog", 12)
dog2 = Dog("Karl", "Cat", 8)

dog1.bark()
dog1.description()
dog2.bark()
dog2.description()
