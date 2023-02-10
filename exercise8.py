# We have following information on countries and their population (population is in crores),
#
# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
# Using above create a dictionary of countries and its population
# Write a program that asks user for three type of inputs,
# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
# add: if user input add then it should further ask for a country name to add.
# If country already exist in our dataset then it should print that it exist and do nothing.
# If it doesn't then it asks for population and add that new country/population in our dictionary and print it
# remove: when user inputs remove it should ask for a country to remove.
# If country exist in our dictionary then remove it and print new dictionary using format shown above in (a).
# Else print that country doesn't exist!
# query: on this again ask user for which country he or she wants to query.
# When user inputs that country it will print population of that country.

nameOfCountry = input("enter either print, add, remove or query : ")
countryPopulation = {'china': 143, 'india': 136, 'USA': 32, 'pakistan': 21}
if nameOfCountry == "print":
    for key in countryPopulation:
        print(key, "=>", countryPopulation[key])
elif nameOfCountry == "add":
    nameOfCountryToAdd = input("enter the name of country you want to add : ")
    if nameOfCountryToAdd in countryPopulation:
        print("name of country already exists.")
    else:
        nameOfCountryToAddPopulation = int(input("enter the population of the new country: "))
        countryPopulation[nameOfCountryToAdd] = nameOfCountryToAddPopulation
        print(countryPopulation)
elif nameOfCountry == "remove":
    nameOfCountryToRemove = input("enter the name of the country you want to remove : ")
    if nameOfCountryToRemove in countryPopulation:
            del countryPopulation[nameOfCountryToRemove]
            print(countryPopulation)
            print(nameOfCountryToRemove, "has been removed")
    else:
         print("country does not exist")
elif nameOfCountry == "query":
    nameOfCountryToQuery = input("enter the name of the country you want to query : ")
    if nameOfCountryToQuery in countryPopulation:
        print(countryPopulation[nameOfCountryToQuery])
    else:
        print("country does not exist in the list")


# You are given following list of stocks and their prices in last 3 days,
#
# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]
# Write a program that asks user for operation. Value of operations could be,
# print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# add: When user enters 'add', it asks for stock ticker and price.
# If stock already exist in your list (like info, ril etc) then it will append the price to the list.
# Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

stocks = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}

def print_stocks():
    for stock, prices in stocks.items():
        avg = sum(prices) / len(prices)
        print(f"{stock} ==> {prices} ==> avg: {avg:.2f}")

def add_stock(ticker, price):
    if ticker in stocks:
        stocks[ticker].append(price)
    else:
        stocks[ticker] = [price]

while True:
    user_input = input("Enter operation (print/add): ")
    if user_input == "print":
        print_stocks()
    elif user_input == "add":
        ticker = input("Enter stock ticker: ")
        price = int(input("Enter stock price: "))
        add_stock(ticker, price)
    else:
        break




# Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area,
# circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them
import math
radius = float(input("enter a value for the radius: "))
def circle_calc(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area, circumference, diameter
    # print ("the area of the circle is: ", area, "the circumference is: ", circumference, "the diameter is: ", diameter)
area, circumference, diameter = circle_calc(radius)
print("Area:", area)
print("Circumference:", circumference)
print("Diameter:", diameter)
