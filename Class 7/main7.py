"""
Exercise #1

Take a list, and append from the end to a new list using a while loop. Print the new list after each append.

Original List:
[1,2,3]

Iteration #1: [3]
Iteration #2: [3,2]
Iteration #3: [3,2,1]

"""
# Forloop method/aproach
"""original = [1, 2, 3]
newList = []
neworiginal = original[::-1]

[3], [3, 2], [3, 2, 1]

for digit in neworiginal:
    newList.append(digit)
    print(newList)
"""


#whileloop aproach
"""original = [1, 2, 3]
newList = []
neworiginal = original[::-1]
i = 0

while len(newList) < len(neworiginal):
    newList.append(neworiginal[i])
    print(newList)
    i += 1


original = [1, 2, 3]
newList = []

i = len(original) -1
# i = 3 - 1 = 2

while i >= 0:
    newList.append(original[i])
    print(newList)
    i -= 1
    # i = i - 1 = 0

original[0] = 1"""

"""word = "dog"
newword = ""

i = len(word) -1

while i >= 0:
    newword += word[i]
    print(newword)
    i -= 1


age = 18

ourBirthday = True

if ourBirthday:
    age = age + 1
    #age - = 1 
    print(age)
    # # new age variable = previous one + 1
    # # previous age  = 18
    # #newage = 18 + 1
    # newAge = age + 1
    # # newAge = 18 + 1 = 19
    # age = newAge
    

i = 0
"""
"""while i <= 10:
    print(i)
    i += 4"""

"""myList = ["Hello", "World"]

for i in myList:
    for j in i:
        print(j)"""


"""
myList = [[["Hello", "World"]]]

for i in myList:
    for j in i:
        for s in j:
            for m in s:
                print(m)
"""

top = ["T-Shirt", "Hoodie", "Sweater"]
bottom = ["Jean", 'Shorts', "Dress"]

combination = 0

for t in top:
    for b in bottom:
        combination += 1

print(combination)

# for b in bottom:
#     print(b)