from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type="ice_cream"):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print(f"{self.name.title()} has the following flavors:")
        for flavors in self.flavors:
            print("   ", flavors.title())
        if (len(self.flavors) < 31):
            print("   "f"... and {31-len(self.flavors)} more")


baskin_robbins = IceCreamStand("baskin-robbins")
baskin_robbins.flavors = ["Chocolate", "Oreo", "Vanilla"]
baskin_robbins.display_flavors()
