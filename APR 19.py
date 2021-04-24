#Homework Takeup

"""
*
&&
***
&&&&
*****
&&&&&&

Observation chart:
L   T   # 
1   *   1
2   &   2
3   *   3
4   &   L
5   *   L
6   &   L

Every odd number will be *, and even will be &

"""

# Standard nested loop triangle
# for i in range(1, 6):
#     for star in range(i):
#         print("*", end="")

#     print("")

#Alternating Triangle
for i in range(1, 10):
    #i represents the layer (L in the chart)
    for star in range(i):
        #On layer i, we want i stars in that layer
        #Check if the layer is even or odd
        #Even:
        if i % 2 == 0:
            print('&', end="") #Prevents printing on the next line
        #Odd:
        else:
            print('*', end="") # Prevents printing on the next line

    print("")

    """
Exercise Warmup:

foods = ['ham', 'Bagels', 'Dumplings', 'bacon', 'apples', 'Pepperoni', 'Noodles', 'eggrolls', 'fish', 'ice cream', 'lobster', 'corn',
         'French toast', 'grapes', 'kiwi', 'jam', 'granola bar', 'asparagus', 'buritto', 'English muffins', 'celery', 'Spaghetti', 'avacado']
drinks = ['Ginger beer', 'fanta', 'Orange Juice', 'A&W Root Beer', 'beer', 'eggnog', 'Diet coke',
          'Carrot juice', 'lime juice', 'strawberry juice', 'Boost Juice', 'Dr. Pepper', 'apple juice']

Given two lists of food and drink, find all combinations in which they go together. However, we are picky, we do not want to eat the same thing that starts with the same letter.

Goal: Find all combinations in which we can eat but doesn't start with the same name
Hint: Some food starts with the same letter but are in different caps (s vs S), but they are still the same letter

"""

foods = ['ham', 'Bagels', 'Dumplings', 'bacon', 'apples', 'Pepperoni', 'Noodles', 'eggrolls', 'fish', 'ice cream', 'lobster', 'corn',
         'French toast', 'grapes', 'kiwi', 'jam', 'granola bar', 'asparagus', 'buritto', 'English muffins', 'celery', 'Spaghetti', 'avacado']
drinks = ['Ginger beer', 'fanta', 'Orange Juice', 'A&W Root Beer', 'beer', 'eggnog', 'Diet coke',
          'Carrot juice', 'lime juice', 'strawberry juice', 'Boost Juice', 'Dr. Pepper', 'apple juice']
temp = []

"""
Observing Chart:
F               D
Spaghetti       strawberry juice

They start with the same letter but in python is case-sensitive (s != S). 
In English s == S same letter

s != S
s == s
S == S

"""

# String is just a collection (list) of alphabets (character)


# upperS = 'S'
# lowerS = 's'

# print(upperS.lower() = lowerS) #We made upper S lower, so lower == lower
# print(lowerS.upper() == upperS) #We made lower S upper case, so upper == upper

for f in foods:
    for d in drinks:
        #We don't want to print this because they start with the same letter.
        if f[0].upper() != d[0].upper():
            print(f, d)
