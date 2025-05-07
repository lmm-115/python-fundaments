# normal list 
from re import L


mystring = 'string'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# with list comprehensions
mystring = 'me'
mylist = [letter for letter in mystring]
print(mylist)

mylist = [x for x in 'word']
print(mylist)

list = [num for num in range(0,11)]
print(list)

# doing operations
list = [num**2 for num in range(0,11)]
print(list)

# just even numbers
list = [x for x in range(0,11) if x%2==0]
print(list)

# difference
celsius = [0,10,20,34.5]
fahrenheit = [( (9/5)*temp + 32) for temp in celsius]
print(fahrenheit)

fahrenheit = []
for temp in celsius:
    fahrenheit.append((9/5)*temp + 32)
print(fahrenheit) 

# the same result but different operations

# nested loops
mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)
