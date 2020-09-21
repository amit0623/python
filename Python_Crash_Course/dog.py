class Dog :
    """ an attempt to model a dog """

    def __init__(self,name,age):
        """Initialize the name and age attributes """
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dig is stillng when the command is fired """
        print(f"{self.name} is now sitting ")
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} has rolled over ")

my_dog = Dog('Willie' , 6 )

print(f"My dog's name is {my_dog.name}")
print(f"My dogs age is {my_dog.age}")
