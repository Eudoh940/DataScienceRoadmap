# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
import math
length = 92
breadth = 48.8
area = length * breadth
print(math.ceil (area))

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
# Find out using python, how many dollars is the shopkeeper going to give you back?
amountOfPacks = 9
cost = 1.49
amnt_paid = 20
value = amnt_paid - (amountOfPacks * cost)
print(value)

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
# If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
# Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
costOfTiles = 500
length = 5.5
area = length**2
total = costOfTiles * area
print(total)

# 4. Print binary representation of number 17
print(bin(17))
