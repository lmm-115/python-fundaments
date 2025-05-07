# TO USE THESE 2 FUNCTIONS IT IS NEEDED TO CONVERT IT
# TO A LIST OR AN ITERABLE (FOR)

# MAP FUNCTION
nums = [1,2,3,4,5]
def square(n):
    return n*n

for i in map(square, nums):
    print(i)

# this is to make it a list 
print(list(map(square, nums)))

# return EVEN if the lenght of the string is even 
# return de index [0] of the string if not
def splicer(x, index=0):
    if index >= len(x):
        return ''
    elif len(x)%2==0:
        return 'EVEN'
    else:
        return x[0]

names = ['Abby', 'Angel', 'Eunice']
print(list(map(splicer,names)))

# FILTER FUNCTION
def even(n):
    return n%2==0

nums = [1,3,4,5,7,8]
res = list(filter(even, nums))
print(res)

# LAMBDA EXPRESSIONS - Lambda expressions basically are "one time use function"
# <<anonymous function>>
# function way to lambda expression
def square(n):
    return n*n

#lambda expression
lambda n: n*n

# example
print(list(map(lambda n:n*n, nums)))
print(list(filter(lambda n:n%2==0, nums)))
print(list(map(lambda n:n[0], names)))
print(list(map(lambda n:n[::-1], names)))