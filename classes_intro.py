#creating a class
class Things:
    pass
#creating a derived class (from base class)
class Inanimate(Things):
    pass

class Animate(Things):
    def exist(self):
      print('Cogito ergo sum')

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
    # usually in life complex functions and actions consist of simpler, iherited functions
    # example - how to use function eat() in eat_leaves_from_trees()
    def eat_leaves_from_trees(self):
        self.eat()
        print('right from the trees')
    def eat_rainbow_from_the_sky(self):
        # TODO - eat() it, for Skittles sake!
    def find_food(self):
      # TODO - move() your ass, find some food, eat() it!
    def dance_jig(self):
      # TODO - move(), move(), move(), move() your body!
