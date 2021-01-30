# word = 'Champion'

# list[start:] Items start through rest of the array
# print(word[1:]) # hampion
# print(word[4:]) # pion

# list[:stop] Item start from beginning, and end at stop - 1
# print(word[:5]) # Champ

# list[start:stop] We start from index at start, and stop at stop -1
# print(word[2:5]) # amp

#list[:] = list (Copies the list)
# print((word[:])
# print(type(word))

# list[start:stop:step] List starts from start, don't go past, skip by step
# print(word[:7:3])



# myList = [1,2,3,4,5]

# print(myList[::-1])

# myList = [10,30, 50, 5, 9]

# maxNum = myList[0]

# for item in myList:
#     if item > temp:
#     temp = item

#     print(maxNum)

# 10 
# 30
# 50 
# 5  <-
# 9

# myNumberList = [10] # max = 10 min = 10
# myNumberList = [] # Not allowed empty list
# myNumberList = [-23, -50] # Allowed Negative

# print(max(myNumberList))# Running the max value
# print(min(myNumberLsit))# Running the min value

# myOddList = [1, 3, 5, 7]
# myEvenList = [2, 4, 6, 8]
# myTensList = [10, 20, 30, 40]
# for oddItem, evenItem, tensItem in zip(myOddList, myEvenList, myTensList):
#     print(oddItem, evenItem, tensItem)

# [1,2,3] + [4,5,6] = [1,2,3,4,5,6] #This is not what zip does
# zip([1,2,3], [4,5,6]) = [1,4], [2,5], [3,6] # This is what zip does

#zip --> We can access the same element at the same index on multiple different lists AT THE SAME TIME

myString = "My name is Sarah"

part1 = ["M", "na", "i", "Sar"]
part2 = ["y", "me", "s", "ah"]
temp = []
for part1Item, part2Item in zip(part1, part2):
    temp.append((part1Item+part2Item)+" ")
    # print(part1Item+part2Item)
    # temp = temp + (part1Item + part2Item) + " " 
    # temp = temp + (part1Item + part2Item)
temp = "".join(temp)
print(temp)

myList = ["Hello", "World", "1234"]

# number = 5
# number = number + 1
# print(number)

# myString = "Hello"
# myString = myString + "World"
# print(myString)

temp = 10

temp += 1
#This is the same as
temp = temp + 1

    
### Homework ###
 
myList = [5, 10, 40, 20, 20, 20, 25, 40, 20]

# Replace only the first occurance of 20 with 100
#Result
# >>>[5, 10, 40, 100, 100, 100, 25, 40, 100]



