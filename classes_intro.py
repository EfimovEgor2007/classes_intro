#creating a class
class Things:
    pass
#creating a derived class (from base class)
class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('breathes')
    def move(self):
        print('moves')
    def eat(self):
        print('eats some food')

class Mammals(Animals):
    def feed_baby_with_milk(self):
        print('feeds the baby with milk')

class Giraffes(Mammals):
    
    # initializing Giraffe with number of spots on it
    def __init__(self,spots):
        self.giraffe_spots = spots
        
    def eat_leaves_from_trees(self):
        self.eat()
        print('right from the trees')
    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat()
    def dance_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
    def get_painted(self):
        self.giraffe_spots += 100
        
# TODO:
# 1 - create class Dogs
# 2 - initialize a Dog with its name, breed and age
# 3 - add some abilities for the Dogs (create some functions)

class Dogs(#...
    
# make a small zoo with Dogs and Giraffes
# pretend that the life goes on


