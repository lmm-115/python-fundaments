# range function 
mylist = [1,2,3]
for num in range(0,10,2): # from 0 to 10 in steps of 2 
    print(num)

# enumerate function 
# with not enumerate function 
index_count = 0 
for letter in 'abcde':
    print('at index {} the letter is {}'.format(index_count,letter))
    index_count += 1 

# with not enumerate function 
index_count = 0 
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

# with enumerate function 
word = 'abcde'
for index,letter in enumerate(word): #return tuples 
    print(index) 
    print(letter)
    print('\n')

# zip function 
mylist1 = [1,2,3] 
mylist2 = ['a','b','c']
for item in zip(mylist1,mylist2):
    print(item)   

print('x' in [1,2,3]) #checks if a string/number is in a list/dictionary 
print('x' in [1,'x','100'])

# max and min functions
mylist = [1,13,17,300]
print(min(mylist))
print(max(mylist))

# import random library 
from random import shuffle # shuffle the values 
from re import M 
mylist = [1,2,3,4,5,6]
shuffle(mylist)
print(mylist)

from random import randint # select only one value of the given range 
print(randint(0,100))
mynum = randint(0,10) # can save the randint function in a variable 
print(mynum)

# input function 
name = input('whats ur name: ')
