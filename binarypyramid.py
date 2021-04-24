# i = 0
# name = "*"
# userinput = int(input("How many layers of \"*\" do you want me to print?"))
# while i <= userinput:
#     print(i * name)
#     i += 1 

# for i in range (6,0,-1):
#     print(i)
# name = "*" * 5
# print(name)
# for i in range (5,0,-1):
#     print(name * i)


# i = 5
# temp = []

# while i >= 1:
#     numberList = (i * "*")
#     i -= 1
#     temp.append(numberList[i])
    

# i = temp
# print(temp)

# i = 0
# while i <= userinput:
#     print(i * name)
#     i += 1 


"""
***** => 0 space, 5 stars
 **** => 1 space, 4 stars
  *** => 2 spaces, 3 stars
   ** => 3 spaces, 2 stars
    * => 4 spaces, 1 star
"""


howManyOddNumbers = int(input("How many odd number do you want in your list:"))
oddList = []

i = 0

while len(oddList) != howManyOddNumbers:
    #If the number is odd
    if i % 2 == 1:
        oddList.append(i)
    i += 1

temp = []
for i in range(len(oddList) -1, -1, -1):
    temp.append(oddList[i])

oddList = temp
print(oddList)

# for numberOfStarsPerLevel in oddList:

#     for theNumberOfStarsOnThisLevel in range(numberOfStarsPerLevel):
#         print(1, end="")
#         print(0, end="")
#     print('')


for I in oddList(1, howManyOddNumbers+1):
    for J in range(1, I+1):
        print(J%2,end="")
    print()


# 1010101010

# Example: [11, 9, 7, 5, 3, 1]
# On the first layer (index 0), we want 11 numbers (1 and 0)

# When solving problems in Python (Any sort of programming), you want to take into consideration, that the solution would work for different scenerios.

