#using general and class functions
def some_random_function():
    print('I am a normal function')

#IMPORTANT! -  all functions take 'self' as an argument
class SomeRandomClass:
    #---------------------!!!here!!!-------------------
    def first_class_function(self):
        print('I am a class function')
    #---------------------!!!here!!!-------------------
    def second_class_function(self):
        return 'I am also a class function'
    pass

#general func
some_random_function()
a = SomeRandomClass()
#class functions
first_func = a.first_class_function
second_func = a.second_class_function
print('new funcs')
first_func()
print(second_func())
print('directly class funcs')
a.first_class_function()
print(a.second_class_function())
