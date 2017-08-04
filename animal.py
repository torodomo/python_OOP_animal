# Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.
# Objective
# The objective of this assignment is to help you understand inheritance. 
# Remember that a class is more than just a collection of properties and methods. 
# If you want to create a new class with attributes and methods that are already defined in another class, 
# you can have this new class inherit from that other class (called the parent) instead of copying and pasting code from the original class. 
# Child classes can access all the attributes and methods of a parent class AND have new attributes and methods of its own, for child instances to call. 
# As we see with Wizard / Ninja / Samurai (that are each descended from Human), we can have numerous unique child classes that inherit from the same parent class.



class animal(object):

    def __init__(self):
        self.health = 0
        self.name = ""
    
    def displayHealth(self):
        print self.name
        print "Health", self.health
        return self

    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 10
        return self


class dog(animal):
    def __init__(self):
        self.name = "My name is Doog"
        self.health = 150

    def pet(self):
        self.health +=5
        return self

dog = dog()
dog.walk().walk().walk().run().run().pet().displayHealth()

class dragon(animal):
    def __init__(self):
        self.name = "Wing"
        self.health = 170

    def fly(self):
        self.health -=10
        print "I AM A DRAAAAAAAGOONNNN"
        return self

dragon = dragon()
dragon.fly().displayHealth()
