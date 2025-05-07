#print
my_name = 'Luis'
age = 19 
print('Hello, my name is' ,my_name ,'and im' ,age) #first way to print using ','
print('Hello, my name is {} and im {}'.format(my_name, age)) # .format method
print('I have a {d} and {m}'.format(d = 'dollar', m = 'money')) # using variables to simplify

# alignment, padding and precision
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.0))

print('\n{0:<8} | {1:^8} | {2:>8}'.format('Left', 'Center', 'Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11, 22, 33))

#value:width.precision f
result = 100/777
print('The result was {}'.format(result))
print('The result was {r:1.3}'.format(r = result))


