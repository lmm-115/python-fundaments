# while loops will continue to execute a block of code while some condition remains True
# syntax 
# while some_boolean_condition:
#   do something
x = 0 
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1 # also written as x += 1 
else:
    print('x is not less than 5 ')

# pass: does nothing at all 
x = [1,2,3]
for item in x: 
    # comment <this comment gives an error cause the indentation expects a "function"
    pass # this keyword allow the comment
print('end of my script')

# continue: goes to the top of the closet enclosing loop 
mystring = 'wanda'
for letter in mystring:
    if letter == 'a':
        continue # basically jumps the value
    print(letter)

# break: breaks out of the current closest enclosing loop 
x = 0 
while x < 5:
    if x == 2:
        break # stops the run 
    print(x)
    x += 1 
