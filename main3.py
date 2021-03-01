words = ['meat', 'sunshine', 'queue', 'horn', 'mobile', 'lighter', 'medicine', 'error', 'height', 'drown', 'trip',
         'major']
temp = []

# for mywords in words:
#     if len(mywords) == 4:
#         temp.append(mywords)
# words = temp 
# print(temp)

words = [mywords for mywords in words if len(mywords) != 4]
print(words)

# [variable for-loop condition]

# myNum = [1, 2, 3, 4, 5, 6, 7]

# myNum = [oddNumber for oddNumber in myNum if oddNumber % 2 != 0]

# ! in Python means not


# Cumulative Sum

myNum = [5, 2, 5, 0, 3, 1, 6, 7]
Output = [myNum[0]]

for i in range(len(myNum)):
    if i == len(myNum) - 1:
        break
    Output.append(Output[i] + myNum[i+1])

print(Output)

