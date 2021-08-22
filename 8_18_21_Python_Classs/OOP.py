class Point:
    x = 2
    y = 5


p1 = Point()
p2 = Point()
p1.x = 12
p1.y = 54
print(p1.x, p1.y)

# class Dog:
#     name = "Rover"
#     color = "Brown"


class Dog:
    def __init__(self, breed):
        self.breed = breed
        self.name = ""
        self.color = ""
        self.weight = 0


d1 = Dog()
d2 = Dog()
d2.name = "Snoopy"
d2.color = "Black and White"

mydog = d2

print(f"{mydog.name} is a {mydog.color} dog")
