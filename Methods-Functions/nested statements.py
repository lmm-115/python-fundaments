# LEGB RULE
"""
Local - Names assignes in any way within a function
        and not declared global in that function

Enclosing function locals - Names in the local scope
        of any and all enclosing functions, from
        inner to outer

Global - Names assignes at the top-level of a module
         file, or declared global ina def within the file

Built-in - Names preassignes in the built-in names
           module: open, range, SyntaxError
"""

# LOCAL > ENCLOSING > GLOBAL > BUILT-IN

# local 
lambda num:num+2

# global
name = 'This is a global string'

def greet():
    
    # enclosing function local
    name = 'Sara'
    
    def hello():

        # local 
        name = 'Soy la "variable" local'
        print('Hola, '+name)
    hello()
greet()

x = 1

def func():
    
    # take the global variable 
    global x
    print(f'This is {x}')

    # local reassignment changes the global value to local
    x = 'this new value'
    print(f'Now x is {x}')

print(func())

# global value changed for the local 
print(x)