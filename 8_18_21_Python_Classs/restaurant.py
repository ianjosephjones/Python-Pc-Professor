class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def __str__(self):
        """This is the self-describing message for the Restaurant class"""
        return f"{self.name} is a {self.cuisine_type} restaurant"


restaurant = Restaurant('Five Guys', 'burger')
print("The restaurant name is:", restaurant.name)
print("The restaurant cuisine is", restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant)


r1 = restaurant
r2 = Restaurant("olive garden", "fake Italian")
r3 = Restaurant("red lobster", "fake seafood")
print(r1)
print(r2)
print(r3)
print('-'*20)
print(r1, r2, r3, sep='\n')

print("-"*10, "loop", '-'*10, '\n')
local_restaurants = [r1, r2, r3]
for lr in local_restaurants:
    print(lr)

print("-"*10, "simplified", '-'*10, '\n')
[print(lr) for lr in local_restaurants]
