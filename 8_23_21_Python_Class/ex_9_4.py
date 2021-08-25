class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, addl_served):
        self.number_served += addl_served

    def __str__(self):
        """This is the self-describing message for the Restaurant class"""
        return f"{self.name} is a {self.cuisine_type} restaurant that has served {self.number_served} happy customers"


restaurant = Restaurant("Ale House", "Pub")
print(restaurant)
print(restaurant.number_served)
restaurant.number_served = 25
print(restaurant.number_served)
restaurant.set_number_served(44)
print(restaurant.number_served)
restaurant.increment_number_served(22)
print(restaurant.number_served)
print(restaurant)
