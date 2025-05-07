# diccionaries
my_dic = {'key1':'value1','key2':'value2'}
print(my_dic['key1'])

prices_lookup = {'apple':'2.99','mango':0.99}
print(prices_lookup['mango'])

#diccionaries within diccionaries
d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}
print(d['k2'])
print(d['k3'])
print(d['k3']['insideKey'])

#re asing variables
d = {'key1':['a','b','c']}
mylist = d['key1']
print(mylist)
letter = mylist[0]
print(letter)
print(letter.upper())

#doing it at once 
print(d['key1'][2].upper())

#add more things to a diccionary 
d['k4'] = 3.14 #this way adds another element to its diccionary
print(d)
#re asign 
d['key1'] = 'heute'
print(d)
#methods with diccionaries 
d.keys() #to show all the keys within the diccionary 
d.values() #to show all the values 
d.items() #to show all of the keys and values that are in


