mylist = [1, 3, 5, 7, 9, 11]
newlist = []
i = len(mylist)-1

while i >= 0:
    newlist.append(mylist[i])
    i-=1
print(newlist)

# Use nested for-loops to create a starts triange

"""

*
**
***
****
*****

for statement:
    for anotherStatement:

**
****
******
********

*
&&
***
&&&&
*****

L   T
1   *
2   &
3   *
4   &
5   *

Use the if something something


"""

# meal = ["Burger", "Pizza", "Hot-dog"]
# drinks = ["Water", "Coke", "Orange juice"]

# for m in meals:
#     for d in drinks
#         print(m, d)

print("Hello", end="")
print("Okay")

letter = ""

# for numberOfStarsPerLevel in range(1,6):
#     # Looping over the number of starts to print for current level
#     # numberOfStarsPerLevel is 2

#     for theNumberOfStarsOnThisLevel in range(numberOfStarsPerLevel):
#         # Printing the stars for the current level
#         print("*", end="")

#     # end = "" means the enxt staement is on the same line
#     # Finished printing star for this level
#     # Print statement automatically goes on a newline, even if there is nothing
#     print('')
#     # We don't have an end = "" il will wrap to teh enxt line
#     # Inline vs Block

letter = ['*', '&', '*', '&', '*']
for numberOfStarsPerLevel in range(1,8):
# Looping over the number of starts to print for current level
# numberOfStarsPerLeve l is 2
    sign = letter[numberOfStarsPerLevel -1]
    for theNumberOfStarsOnThisLevel in range(numberOfStarsPerLevel):
        # Printing the stars for the current level
        print(sign, end="")

    # end = "" means the enxt staement is on the same line
    # Finished printing star for this level
    # Print statement automatically goes on a newline, even if there is nothing
    print('')
    # We don't have an end = "" il will wrap to teh enxt line
    # Inline vs Block




