#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities
#
# Computer Science 111
#
#Name: Batyr Issabekov

import math

def display_menu():
    """ prints a menu of options
    """
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')

    ## Add the new menu options here.

    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return

    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.

def avg_price(prices):
    """takes a list and returns the average price"""
    sum = 0
    for i in prices:   #for loop
        sum += i       #adds i to the sum
    return (sum/len(prices))  #calculated the average by dividing
                                #sum by lenprices

def std_dev(prices):
    """returns the standard deviation of the prices"""
    sum = 0
    for i in prices:                    #element for loop
        L_avg = avg_price(prices)       #assigned average by using previous func
        numerator= (i - L_avg) **2      #calculates the numerator
        sum+= numerator                #sums due to sigma notation
    sum /= len(prices)                #divides by denominator
    return math.sqrt(sum)            #returns the square root

def max_day(prices):
    """returns the day of the maximum price"""
    day = 0                       #day is 0
    for i in range(len(prices)):  #index based for loop
        if prices[i]>prices[day]:   #if price of current day more than 0 from
                                    #start
            day =i                  #that day is assigned to  index
    return day                     #returns the day (index)

def any_below(prices, threshold):
    """determines if there are any prices below the threshold"""
    for i in prices:
        if i<threshold:   #if any number is less than threshold
            return True   #returns True
    return False   #otherwise, False

def find_plan(prices):
    """finds the best days on which to buy and sell stock whose prices"""


    """n = 0
    prev= prices[n]
    next = prices[n+1]
    lowest = 0
    highest = 0"""
    profit = 0     #profit is 0
    for i in range(len(prices)):    #index loop for i in prices
        for e in range((i+1),(len(prices))):    #index loop starting from
                                                #prices[1]
            if (prices[e]-prices[i])>profit:   #if difference larger than profit
                profit = prices[e]-prices[i]  #assign profit to that difference
                buy = i                      #buy day is the index i
                sell = e                    #sell day is the index e

    return [buy,sell,profit]




def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            avg = avg_price(prices)
            print('The average price is', avg)
        elif choice == 4:
            std =std_dev(prices)
            print('The standard deviation is', std)
        elif choice == 5:
            max_d = max_day(prices)
            print('The max price is',prices[max_d], 'on day',max_d)
        elif choice == 6:
            threshold = int(input('Enter the threshold: '))
            th = any_below(prices,threshold)
            if th == True:
                print('There is at least one price below', threshold)
            else:
                print('There are no prices below', threshold)
        elif choice == 7:
            time_travel = find_plan(prices)
            print('Buy on day',time_travel[0],'at price',prices[time_travel[0]])
            print('Sell on day',time_travel[1],'at price',prices[time_travel[1]])
            print('Total profit:',time_travel[2])

        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
