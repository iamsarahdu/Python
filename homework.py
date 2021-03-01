# def FunctionNames(namesLists):
#     nameSet=list(set(namesLists))
#     print("NameSet:",nameSet)


# namesLists = ["Sarah", "Jessica", "Sophia", "Sarah", "Jessica"]
# FunctionNames(namesLists)




# myList = [1, 2, 2, 3, 5, 7, 7]

# temp = []
# for item in myList:
#     if item not in temp:
#         temp.append(item)

# myList = temp

# ### Homework ###

# # Replace only the first occurance of 20 with 100
# #Result
# # >>>[5, 10, 40, 100, 100, 100, 25, 40, 100]

# myList = [5, 10, 40, 20, 20, 20, 25, 40, 20]


# for n, i in enumerate(myList[:4]):
#     if i == 20:
#         myList[n] = 100 
        
# print(myList)

# # Get the first index of 20

# fruitList = ["mango", "apple", "banana", "cherry", "apple", "apple", "apple", "apple"]

# print(fruitList.index("apple"))
    
# myList = [1, 2, 3, 4, 5, 3, 6, 3]

# print(myList.index(3))

# #list.index method returns the index of the FIRST occurance.


# print(myList)

myList = [5, 10, 40, 10, 20, 20, 25, 20, 40, 20]
temp = []

# firstOccuranceIndex = myList.index(20) # The index of the first occurance of number 20

# myList[firstOccuranceIndex] = 100

# print(myList)

# firstOccuranceIndex = myList.index(20)

# print(firstOccuranceIndex)

###ALTERNATIVE###D

for num in myList: # <- We are iterating over the list (myList)
    # Remove ALL 20 with 100
    
    #If number is 20, replace it with 100 (Appnd to the temp list)
    if num == 20:
        temp.append(100)
    # If number is not 20 it can remain how it is
    else: 
        temp.append(num)

# Replace myList with whatever we've modified inside the Loop (We cannot modify the List inside the Loop)



# You cannot modify a list while iterating over it
# Inside Loop, we didn't touch myList, it remains original
# Because we didn't touch myList, we need to replace it with temp <- Modifying myList

# Set myList ot temp, which is whatever we've done inside the loop.

# We cannot make modifications while looping over it. Python does not like that.

# myList = temp

# for num in myList:
#     if num == 20;
#     myList.remove(num)


# a = 5
# b = 8
# temp = a # 5

# # To swap, we want a = 8, b = 5;

# a, b = b, a 

# print(a,b)

# b = a #5

# a = temp
# print(myList)

# b = temp

print(myList)

