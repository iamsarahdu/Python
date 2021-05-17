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

#First Step
howManyOddNumbers = int(input("How many layers do you want in your trangle:"))
oddList = []

i = 0

#Step 2 finished
while len(oddList) != howManyOddNumbers:
    #If the number is odd
    if i % 2 == 1:
        oddList.append(i)
    i += 1

# Step 3
temp = []
for i in range(len(oddList) -1, -1, -1):
    temp.append(oddList[i])

oddList = temp

# for numberOfStarsPerLevel in oddList:
#     for theNumberOfStarsOnThisLevel in range(numberOfStarsPerLevel):
#         print(1, end="")
#         print(0, end="")
#     print('')




# 1010101010

# Example: [11, 9, 7, 5, 3, 1]
# On the first layer (index 0), we want 11 numbers (1 and 0)

# When solving problems in Python (Any sort of programming), you want to take into consideration, that the solution would work for different scenerios.


# April 26

"""

I   N
0   1
1   0
2   1
3   0
4   1
5   0

Odd number will be 0
Even number will be 1

"""

layersToBePrinted = []

"""
      *
     ***
    *****
   *******
"""

# Should be the same length as layers (number) we inputted (howManyOddNumbers)
layersToBePrinted = []

"""
* => '*'
** => '**'
*** => '***'

['*'], '**', '***]

If we iterate over this list:

*
**
***

"""

numOfOneZeros = 11

# 4th step ( THE ACTUAL layers)

for numOfOneZeros in oddList:
    # Either we start or we finished last iteration,
    currentLayer = ''
    for i in range(numOfOneZeros):
        # i is the index of expected outcome
        # expected outcome is alternating 1 and 0, 
        # odd index will be be 1
        if i % 2 == 0:
            # Should be 1
            currentLayer += "1"
        else:
            # Should be 
            currentLayer += "0"
        
    # Our loop is over
    #After we make our current layer
    layersToBePrinted.append(currentLayer)


# print(layersToBePrinted) # LIST


"""
Prediction
If we want 3 layers, what does the triangle look like?

10101
101
1

1st: Determine the first 3 odd numbers: 1, 3, 5
2nd: The triangle is upside down: 5,3,1

5: 10101
3: 101
1: 1


10101
 101
  1


5 layers:

101010101
1010101
10101
101
1

layers = ["101010101", "1010101", "10101", "101", "1"]

3 steps to get to the above:

1st: Determine how many layers (5)
2nd: Determine 5 odd numbers: 1, 3, 5, 7, 9
3rd: Reverse: 9,7,5,3,1(These numbers are represent how many 1, 0 will be in each ""/layer.)
4th: Convert that list into the ACTUAL LAYER.
"""

# 5th Step: print our layers one at a time

space = 0

for layer in layersToBePrinted:
    # 6th step, center our printed layers
    print(" "*space+layer+" " *space)
    space += 1
    







"""
Centering Example:

10101 => 0 space
_101_ => 1 space
__1__ => 2 space

Everytime we go down a layer, we add a space beside (Both left and right)

"""



