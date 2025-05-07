# indexing[]
mystring = 'Hello World'
print(mystring[0])

#len to split string
def split_string(value):
    string1 = value[:len(value)//2]
    return string1
print(split_string("Cinematográfico"))

# slicing[]
mystring = 'abcdefghijk'
print(mystring[2:]) #this prints all after the index number
print(mystring[:3]) #this prints all before the index number
print(mystring[3:6])
print(mystring[1:3])
print(mystring[::2]) #stepsize
print(mystring[2:9:2])#start:stop:step  
print(mystring[::-1]) #reverse the string

#concatenate
name = "Sam" 
# name[0] = "P"
print('P' + name[1:])

letter = 'z'
print(letter * 10) #variable 'x' times 

x = 'hello WORLD' 
print(x.upper())
print(x.lower()) 
print(x.split())

