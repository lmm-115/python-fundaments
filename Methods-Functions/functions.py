def say_hello(name='default'): # when there is no specific name will print default
    print(f'Hello {name}')
print(say_hello('Alfredo'))

def add_num(num1,num2):
    return num1+num2
print(add_num(7,5))

# functions with logic 
def even_check(number):
    return number % 2 == 0
print(even_check(258))
print(even_check(15))

# return true if any number is even inside a list 
def check_even_list(num_list):
    # "i" represent every element
    for i in num_list:
        if i % 2 == 0:
            return True
        else: 
             pass
    
    return False       
print(check_even_list([1,3,5,7]))
print(check_even_list([1,3,5,8]))

# return all the even number in a list 
def check_even_list(num_list):
    # placeholder variables
    # useful for store values at the end of the process
    even_numbers= []
    
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers 
print(check_even_list([1,2,3,4,5,6,7,8,9,10]))



