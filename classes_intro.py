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
    pass

class Mammals(Animals):
    pass

class Giraffes(Mammals):
    pass

#creating an object of a given class
reginald = Giraffes()
