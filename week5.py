# Assignment 1
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method move()")

class Car(Animal):
    def move(self):
        print("Driving")

class Plane(Animal):
    def move(self):
        print("Flying")

# Creating instances of each class and calling the `move` method on them
my_car = Car()
my_plane = Plane()

# Using a list to demonstrate polymorphism in action
vehicles = [my_car, my_plane]

# Calling the move method for each vehicle
for vehicle in vehicles:
    vehicle.move()

# Output:
# Driving
# Flying


# Activity 2
class Mobile:
    def move(self):
        raise NotImplementedError("Subclass must implement move()")


class Dog(Mobile):
    def move(self):
        print("Running")


class Cat(Mobile):
    def move(self):
        print("Pouncing")


class Fish(Mobile):
    def move(self):
        print("Swimming")


# Creating instances of each class
pet_dog = Dog()
pet_cat = Cat()
pet_fish = Fish()


# A list of pets
pets = [pet_dog, pet_cat, pet_fish]


# Using a function to call the `move` method for each pet
def make_pet_move(pet):
    pet.move()


# Looping over the pets and making each one move
for pet in pets:
    make_pet_move(pet)


# Output:
# Running
# Pouncing
# Swimming
