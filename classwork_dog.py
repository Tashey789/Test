class Dog:
    def __init__(self, name, colour, age):
        self.name = name
        self.colour= colour
        self.age = age

dog1= Dog('dawa', 'brown', 3)
dog2 = Dog('nima', 'orange', 5)
dog3 = Dog('blacky', 'black', 3)

print(dog1.name, dog1.colour, dog1.age)
print(dog2.name, dog2.colour, dog2.age)
print(dog3.name, dog3.colour, dog3.age)