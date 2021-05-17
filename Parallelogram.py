widthinput = int(input("How long do you want your parallelogram's width to be?"))
heightinput = int(input("How long do you want your parallelogram's height to be?"))
characterinput = input("Which character do you want to use to print out your parallelogram?")

while len(characterinput) != 1:
    print('We cannot print that, please try again:')
    characterinput = input("Which character do you want to use to print out your rectangle? \n")
    
slantorientation=input("Do you want to slant the parallelogram to the right or left?\n")

possible_orientations = ["left", "right", "Left", "Right"]
while not slantorientation in possible_orientations:
    slantorientation = input("Try again: ")

print("Generating shape now...")

if slantorientation == 'right':
    space = 0
elif slantorientation == 'left':
    space = heightinput - 1   
for height in range(heightinput):
    for width in range(widthinput):
            if width == 0:
                print(" "*space + characterinput, end="");
            else:
                print(characterinput, end="");
    if slantorientation == 'right':
        space += 1
    elif slantorientation == 'left':
        space -= 1     
    print('')

# for width in range(widthinput):
#     print (width);

# for slant in slantorientation:
#     if slantorientation == slant:
#         print(" "*space)
#         space += 1

"""
4 Inputs:
- Width
- Height
- Left right
- Character
"""
