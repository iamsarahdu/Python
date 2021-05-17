numOfOneZeros = 11

for i in range(numOfOneZeros):
    # i is the index of expected outcome
    # expected outcome is alternating 1 and 0, 
    # odd index will be be 1
    if i % 2 == 0:
        print(1, end="")
    else:
        print(0, end="")


layers = ["*", "**", "***"]

# We want print each layer at a time

for layer in layers:
    print()


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

inp = 3 # If we wnat three layers (Give us 3 odd numbers)

numPerLayer = [5, 3, 1] 

layers = ["10101", "101", "1"] # The actual we will print

"""

  *
 ***
*****

*****
***
*
Into
*****
 ***
  *

"""

space = 0 #Space on the first layer, which will always be 0

#
layer = ['*', '***', '*****']

for layer in layers:
    print()
