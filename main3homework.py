
myNum = [5, 2, 5, 0, 3, 1, 6, 7]

n1 = myNum[0]
n2 = myNum[1] + n1
n3 = myNum[2] + n2
n4 = myNum[3] + n3
n5 = myNum[4] + n4
n6 = myNum[5] + n5
n7 = myNum[6] + n6
n8 = myNum[7] + n7
print(n1, n2, n3, n4, n5, n6, n7, n8)  



myNum = [5, 2, 5, 0, 3, 1, 6, 7]
Output = [myNum[0]]

for i in range(len(myNum)):
    if i == len(myNum) - 1:
        break
    Output.append(Output[i] + myNum[i+1])

print(Output)