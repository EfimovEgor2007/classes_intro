#creating a class
class Things:
    pass

#creating a derived class (from base class)
class Inanimate(Things):
    pass

class Animate(Things):
    # example of a class function
    def exist(self):
        print('Cogito ergo sum')

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    # TODO - create three functions for this class: move(), eat(), breathe()
    pass

class Mammals(Animals):
    # TODO - create one function for this class: feed_baby_with_milk()
    pass

class Giraffes(Mammals):
    # TODO - create one function for this class: eat_leaves_from_trees()
    pass
