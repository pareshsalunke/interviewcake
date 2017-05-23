def my_function(arg):
    # write the body of your function here
    smallest = arg[0]
    index = 0

    for idx,price in enumerate(arg):
        if smallest > price:
            smallest = price
            index = idx
	
    highest = arg[index]
    for idx in range(index,len(arg)):
        if highest < price:
            highest = arg[idx]
            
    max_profit = highest - smallest
        
    return 'running with %d' % max_profit

# run your function through some test cases here
# remember: debugging is half the battle!
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print my_function(stock_prices_yesterday)
