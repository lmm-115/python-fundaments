#lists 
my_list = ['string',17,30.1] #lists can save different data types
mylist = ['one','two','three']
print(mylist[0])

another_list = ['four','five']
print(mylist + another_list)

new_list = mylist + another_list
print(new_list)

# change index string/number
new_list[0] = "ONE ALL CAP"
print(new_list)

new_list = [1,2,[3,4,'hello']]
new_list[2][2] = 'goodbye' #using index to change hello
print(new_list)

# append method
new_list.append('six')
print(new_list) # will add 'six' by the append function

# pop method
new_list.pop()

new_list.pop(0)

# sort method (sort by name or number)
new_list = ['a','x','f','y']
new_list.sort

list1 = [2,1,3,7,5]
print(sorted(list1)) # built in function (kinda easy) 

# reverse method (reverse everything)
new_list.reverse()
print(new_list)