# Print square of all numbers between 1 to 10 except even numbers

# After flipping a coin 10 times you got this result
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads

results = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
heads = 0
tails = 0

for i in results:
    if i == "heads":
        heads += 1
    elif i == "tails":
        tails += 1

print("Number of heads:", heads)
print("Number of tails:", tails)


# # Print square of all numbers between 1 to 10 except even numbers
for i in range (1, 11):
    if i % 2 == 0:
        continue
    print(i ** 2)

# Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
# If expense is not found then it should print that as well.

months = ["january", "february", "march", "april", "may"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = int(input("enter expense number: "))

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break
if month != -1:
      print(f'You spent {e} in {months[month]}')
else:
    print(f'You didn\'t spend {e} in any month')


# Write a program that prints following shape
#
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    print("*" * i)