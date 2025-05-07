#SYNTAX OF A FOR LOOP 
# my_iiterable = [1,2,3]
# for item_name in my_iterable:
#   print(item_name)

lista = [1,2,3,4,5] 
for num in lista:
    print(num)
print('even') 

for num in lista:
    #check for even 
    if num % 2 == 0:
        print(num) 
    else:
        print(f'Odd Number: {num}') #what is the function of 'f'??

list_sum = 0 
for num in lista:
    list_sum = list_sum + num 
    print(list_sum) #while is in show us the running task
print (list_sum) # show the final result without the running task

string = 'Hello World' 
for letter in string:
    print(letter)

mylist = [(1,2),(3,4),(5,6),(7,8)] # a list of tuples
for item in mylist:
    print(item) #prints the tuples
for a,b in mylist:
    print(a) # use this if only wants the first element
    print(b) # use this if only wants the second element

# for using dictionaries
d = {'k1':1,'k2':2}
for item in d:     # this will only print the keys
    print(item) 
for item in d.items(): # .items method will iterate the keys and values 
    print(item) 
for item in d.values():
    print(item)
