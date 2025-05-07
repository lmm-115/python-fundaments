#sets = are unoreder collections of unique elements
myset = set()
print(myset) #empty
myset.add(1)
print(myset)
myset.add(2)
myset.add(2)
print(myset) #only appears one 2 because sets can only contain unique elements

mylist = [1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))#will only print the unique sets