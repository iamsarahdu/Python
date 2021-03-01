# Homework takeup

#  numList = [3, 7, 0, 10, 9, 0, 5]
#  output = []

#  for i in range(-1, len(numList) -1):
#      if i == -1:
#          output.append(numList[0])
#      else:
#          if i == len(numList) -1:
#              break
#          output.append(output[i] + numList[i+1])

#  print(output)

# numList = [3, 7, 10, 0,  9, 9, 5]
# output = []

# for i in range(-1, len(numList) -1):
#     if i == -1:
#         output.append(numList[0])
#     elif numList[i+1] == 0:
#         break
#     output.append(output[i] / numList[i+1])

# print(output)

numList = [3, 7, 10, 9, 0, 9, 5]
output = []
for i in range(-1, len(numList)-1):
    if i == -1:
        output.append(numList[0])
    else:
        if numList[i+1] != 0:
            output.append(output[i] / numList[i+1])
        else:
            break
print(output)


# numList = [1, 2, 3, 4, 5, 6sssss]

# numList[-1] = 1

# numList = [1,2,3,4,5,6]

# for i in range(len(numList)-1):
#     print(f"Inxex:i, Number: numList[i]")




