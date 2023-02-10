#1.  Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to
# Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
# For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai
# and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
cityName1 = input("enter city name :")
if cityName1 in india:
    print("it is found in india")
elif cityName1 in pakistan:
    print("it is found in pakistan")
elif cityName1 in bangladesh:
    print("it is found in bangladesh")
else:
    print("It cannot be found anywhere")
cityName2 = input("enter another city name :")
if cityName1 in india and cityName2 in india:
    print("both cities are in india")
elif cityName1 in pakistan and cityName2 in pakistan:
    print("both cities are in pakistan")
elif cityName1 in bangladesh and cityName2 in bangladesh:
    print("both cities are in bangladesh")
else:
    print("they are not in the same country")


#2.  Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal

sugarLevel = int(input("enter your fasting sugar level :"))
sugarLevel in range (80, 100)
if sugarLevel < 80:
    print("sugar is low")
elif sugarLevel > 100:
    print("sugar is high")
else:
    print("it is normal")