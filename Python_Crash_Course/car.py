class Car:
    """A simple attempt to reresent a car """

    def __init__(self, make, model, year):
        """Initialize the attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        # init an attribute which is not passed as parameter.
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the card average """
        print(f"This car has {self.odometer_reading} miles on it ")
    def update_odometer(self,mileage):
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(30)
my_new_car.read_odometer()
my_new_car.increment_odometer(20)
my_new_car.read_odometer()