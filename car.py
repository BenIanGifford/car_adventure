class car():
        """Your car."""

        def __init__(self, make, model, year, fuel_capacity):
            """Atributtes of your car, fuel in gallons."""
            self.make = make
            self.model = model
            self.year = year
            self.fuel_capacity = fuel_capacity
            self.fuel_level = 0
            
        def fill_tank(self):
            """Fill up your gas."""
            self.fuel_level = self.fuel_capacity
            print("Fuel tank is full")

        def drive(self):
            """Drive your car"""
            print("The car is moving")
            self.fuel_level = self.fuel_level

        def specs(self):
            print(self.year, self.make, self.model, self.fuel_capacity, "Gallons")
