# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
# Equation of an area of a triangle is,
# area = (1/2)*base*height
#
base = int(input("enter the base"))
height = int(input("enter the height"))
def calculate_area(base, height):
    area = (1/2)*base*height
    return area
print(calculate_area(base, height))


# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
# Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

shape = input("what shape area do you want to calculate for? you can only type rectangle or triangle ")
if shape == "rectangle":
    length = int(input("enter the length : "))
    breadth = int(input("enter the breadth : "))
    def rectangle(length, breadth):
      recArea = length * breadth
      return recArea
    print(rectangle(length, breadth))

else:
    shape == "triangle"
    base = int(input("enter the base"))
    height = int(input("enter the height"))


    def calculate_area(base, height):
        area = (1 / 2) * base * height
        return area

    print(calculate_area(base, height))

# Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print
#
# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

num = int(input("enter a number: "))
def print_pattern(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print ("*", end = " ")
        print("")
print_pattern(num)