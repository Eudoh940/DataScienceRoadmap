# base = 10
# height = 5
# area = 1/2 * (base * height)
# print("Area of our triangle is: ", area)


# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# simple fun program with if statements and also have a list
# ibibio = ["Afang", "Atama", "Okro", "Afia Efere", "Ekpang Nkukwo"]
# igbo = ["Egusi", "Oha", "Ofe Onugbu", "Nkwobi", "Abacha"]
# yoruba = ["Ewedu", "Ewa Agoyin","Amala", "Efo"]
#
# dish = input("Enter a dish name: ")
# if dish in ibibio:
#     print("ibibio")
# elif dish in igbo:
#     print("igbo")
# elif dish in yoruba:
#     print("yoruba")
# else:
#     print("Based on little knowledge I have, I don't know which cuisine is", dish)

# Problem: Store monthly expenses in a list and find out total expenses for all months
# exp = [2340, 2500, 2100, 3100, 2980]
# total = 0
# for item in exp:
#     total = total + item
# print(total)


# for num in range(1, 11):
#     print(num * num)
#
# exp = [2340, 2500, 2100, 3100, 2980]
# total = 0
# for i in range (len(exp)):
#     print('Month:', (i + 1), 'Expense:', exp[i])
#     total = total + exp[i]
# print('Total expense is:', total)

# key_location = "chair"
# locations = ["garage", "kitchen", "bedroom", "chair", "toilet", "study"]
# for location in locations:
#     if location == key_location:
#         print("Key has been found in", location)
#         break
#     else:
#         print("key is not found in", location)

# square number with for loop
# for num in range(1, 6):
#     if num%2 == 0:
#         continue
#     print(num*num)


# while loop
# Dictionaries/ Tuples
# d = {"tom": "0908465", "bob": '078934', "col": '07089', "lip": "4567"}
# for key in d:
#     print("key:",key, "value:",d[key])
#
# print("james" in d)
# print(d.clear())

import calendar
cal = calendar.month(2023, 1)
print(cal)
print(calendar.isleap(2023))
def come(a, b):
    return a * b
print(come(4, 5))

import math
print(math.sqrt(78))
print(math.pow(2, 5))
print(dir(math))
