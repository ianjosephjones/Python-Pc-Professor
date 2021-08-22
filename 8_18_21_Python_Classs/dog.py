class Dog:
    def __init__(self, breed, name, color="brown", weight="5"):
        self.breed = breed
        self.name = name
        self.color = color
        self.weight = weight
        self.age = 0

    def set_age(self, age):
        self.age = age

    def happy_birthday(self):
        self.age += 1

    def sit(self):
        print(f"{self.name} is sitting")

    def __str__(self):
        my_description = f"{self.name} is a {self.color} {self.breed} weighing {self.weight} pounds"
        if (self.age > 0):
            my_description += f" who is {self.age} years old"
        return my_description


mydog = Dog("Mutt", "Odie")
print(mydog.breed)
mydog.sit()

charlie_dog = Dog("Beagle", "Snoopy", "Black and white", 12)
charlie_dog.age = 5
print(charlie_dog.breed)
charlie_dog.sit()

print(mydog)
print(charlie_dog)

mydog.set_age(8)
print(mydog)

charlie_dog.happy_birthday()
print(charlie_dog)
