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

# --- TODO - would this code work now?
reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()
harold = Giraffes()
harold.move()
# ---

# not all the Giraffes are created equal
oswald = Giraffes(100)
gertrude = Giraffes(150)
print(oswald.giraffe_spots)
print(gertrude.giraffe_spots)

# you've been (heavily) spotted!
oswald.giraffe_spots += 200

# evolve
gertrude.get_painted()

# who's the boss now?!
print('Oswald',oswald.giraffe_spots)
print('Gertrude',gertrude.giraffe_spots)
