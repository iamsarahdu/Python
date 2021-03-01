# # myList = []

# # for i in range(0, 10):
# #     myList.append(i)
    

# # print(myList)

# # Lsit comprehension


# #[variable, loop, condition]

# # myList = [x for x in range(0, 10)]

# # for grade in studentGrade (list)

# print(list(range(10)))

# # 0
# # # 1
# # # 2
# # # 3
# # # 4
# # # 5
# # # 6
# # # 7
# # # 8
# # # 9

# # print(5 % 2) #This is how you get the remainder of a number

# # evenList = [x for x in range(21) if x % 2 == 0]

# # # evenList = [All numbers(x) for the numbers between 0 and 20 (x for x in range(101) if x % 2 == 0), if the number divisible by two, its remainder must be zero or in other words it is an even  number]

# # print(evenList)

# # print(10 % 3)

# # # % is the operator for modulus, it gets the remainder when divided



# # # I want to filter out (remove) all odd numbers -> [44, 14, 10]

# # myNumbers = [allEvenNumbers for allEvenNumbers in myNumbers if allEvenNumbers % 2 == 0]

# # print(myNumbers)

# # for i in ______________________(Whatever is in the blank must be an iterable object)

# #Iterable objects:
# # - Set, list, tuple, string, range

# myString = "Hello"

# # # I want to print myString as a list.

# # print(type(list(myString))) #we are converting myString into a list, and then print

# # myTRang = (1,3,4,5,34535,45,73,4,1)

# # # myTuple = list(myTuple) # Now this is a list
# # # myTuple[0] = 10 # Make the modification
# # # myTuple = tuple (myTuple)

# myRange = range(10) #This is a range (The range between 0 and 9 (10numbers)) # A sequence (iterable) of number in a given range or a step

# print(myRange) # Before conversion
# myRange = list(myRange) #Now this is a list

# print(myRange) #After conversion

# myRange = list(range(10)) # Doable action

# print(myRange)

# numberBank = list(range(101))

numberBank = int(input("What is the number range you want?"))

numberRange = list(range(numberBank))

# numberBank = list(range(101))

NeedsToBeDivisibleBy = int(input("What number do you what your number to be? "))

numberBank = [theNumber for theNumber in numberRange if theNumber % NeedsToBeDivisibleBy == 0]

print(numberBank)