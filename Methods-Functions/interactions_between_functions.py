

from random import shuffle 

example = [1,2,3,4,5,6,7]
result = shuffle(example) # this will not shuffle the list 
print(result) 

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(example)
print(result)

mylist = [' ','O',' ']
shuffle_list(mylist)
def player_guess():
    
    guess = ''
    
    while guess not in ['0','1','2']:
        guess == input("Pick a number: 0, 1 or 2")
    
    return int(guess)
    
my_index = player_guess()
print(my_index)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct')
    else:
        print('wrong guess')
        print(mylist)
print(check_guess(1,2))