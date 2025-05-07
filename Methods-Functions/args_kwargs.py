# args = arguments, kwargs = keywords arguments 
from re import A


def myfunc(a,b):
    # returns 5% of the sum of a and b
    return sum((a,b)) * 0.05
print(myfunc(40,60))

def myfunc_1(a,b,c = 0, d = 0):
    return sum ((a,b,c,d)) * .5 
print(myfunc_1(60,40,100))

# NOTE: Parameters only admit 5 parameters, when you try to use 6 it gives you an error

# args: indefinite parameters (TUPLE)
def myfunc(*args): # the word 'args' can be any other word
    return sum(args) * .5
print(myfunc(40,60,100,200,100,100,100))

def myfunc(*args): 
    for item in args:
        print(item)
print(myfunc(40,60,100,200,100,100,100))

# kwargs {DICTONARY}
def myfunc(**kwargs):
    print(kwargs) #just a dictionary
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format((kwargs['fruit']))) # .format 
    else: 
        print('I did not find any fruit here')
print(myfunc(fruit = 'apple', veggie = 'lettuce'))

# combining both
def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('i would like {} {}'.format(args[0],kwargs['food']))
print(myfunc(10,20,30,fruit = 'orange', food = 'eggs', animal = 'dog'))



