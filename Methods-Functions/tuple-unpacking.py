stock_prices = [('aapl',200,),('goog',400),('msft',600)]
for item in stock_prices:
    print(item)

# tuple unpacking
for ticker,price in stock_prices:
    print(ticker)
    print(price+(.1*price))

work_hours = [('abby',7),('billy',13),('cassie',17)]
def employee_check(work_hours): 
    current_max = 0 
    employee_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_month = employee
        else:
            pass
 
    # Return  
    return (employee_month,current_max)
print(employee_check(work_hours))

# check tuple unpacking 
result = employee_check(work_hours) # prints all the tuple
name,hours = employee_check(work_hours) # can print either name or hours
print(name)
print(hours) 