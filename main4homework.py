numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = []
evenNumbers = []

for i in range(-1, len(numList) -1):
    if i == -1:
        output.append(numList[0])
    elif i%2 == 0:
        output.append(i * (numList[1:]))
    elif i%2 != 0:
        output.append('')
    else:
        if i == len(numList) -1:
            break
        output.append(output[i] * numList[i+1])
print(output)