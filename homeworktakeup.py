# myList = [10, 20, 20, 30, 40]
# temp = []

# for num in myList:
#     if num == 20:
#         temp.append(100)
    
#     else:
#         temp.append(num)
# myList = temp

# print(myList)





# #The logic of only replacing the first occurance.
# # If I didn't replace a 20: replace 20
# # Else: don't replace it 

# did_I_replace_it = False

# for num in myList:
#     if num == 20:
#         if not did_I_replace_it: # I did not  replace it yet
#             temp.append(100)
#         else: # I already replaced it
#             temp.append(num)
#     else:
#         temp.append(num)
# myList = temp

# We cannot make modifications while looping over it. Python does not like that.
# for num in myList
#   if num == 20:
#       myList. remove(num) <-- DOESN'T WORK



### HOMEWORK ###

studentGrade = [55, 80, 67, 75, 92, 99, 43, 85, 78]
temp = []

for grade in studentGrade:
    if grade <= 100 and grade >= 80:
        temp.append('A')
    elif grade <= 80 and grade >= 70:
        temp.append('B')
    elif grade <= 70 and grade >= 60:
        temp.append('C')
    elif grade <= 60 and grade >= 50:
        temp.append('D')
    elif grade <=50:
        temp.append('F')


studentGrade = temp
print(temp)
# # Replace all number grade with letter

# # 80 - 100: A
# # 70- 80: B
# # 60 - 70: C
# # 50 - 60: D
# # BELOW 50: 7(Fail)

# # studenGrade = [D, A, C, B, A, A, F, A, B]

# # If a number is between two numbers:

# grade = 75

# # If grade is between 70 and 80, it's a B right

# #if grade < 80 and grade is => 70:
#     # Number needs to be smaller tha 80 and greater than 70 (Number is between 70 and 80)
#     # This means grade is between 70 and 80
