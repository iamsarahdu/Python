def FunctionNames(namesLists):
    nameSet=list(set(namesLists))
    print("NameSet:",nameSet)


namesLists = ["Sarah", "Jessica", "Sophia", "Sarah", "Jessica"]
FunctionNames(namesLists)




myList = [1, 2, 2, 3, 5, 7, 7]

temp = []
for item in myList:
    if item not in temp:
        temp.append(item)

myList = temp

print(myList)
