numberList = [2, 4, 6, 10, 34, 21]

# Reverse : 21, 34, 5, 10, 6, 4, 2

temp = []

for i in range(len(numberList) -1, -1, -1):
    temp.append(numberList[i])

numberList = temp
print(temp)
   