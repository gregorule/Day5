#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
from abc import ABC, abstractmethod

class Mammal(ABC):
    produce_milk = True
    fur = True
    lay_egg = False
    babies = 0

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def speak(self):
        pass

    extinct = False

class Cat(Mammal):
    def eat(self):
        return "Meat"

    def speak(self):
        return "Meow"

class Lion(Cat):
    def reproduce(self):
        self.babies += 3

    def speak(self):
        return "Roar"

class domestic(Cat):
    def reproduce(self):
        self.babies += 6

class Monotreme(Mammal):
    lay_egg = True

class platypus(Monotreme):
    def reproduce(self):
        self.babies += 2

    def eat(self):
        return "Insects"

    def speak(self):
        return "Purr"


print(platypus.speak("self"))
print(Lion.babies)

