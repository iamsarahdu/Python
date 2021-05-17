"""
Rectangle


Goal:
Input:
- 4 (width)
- 2 (height)
- * (char)

Output:

****
****

Step:
1. Ask the user: width, height, character (Taking input)
    - Only allow character input to be 1 caharacter, *, &
    - Hotdog is not a width: Handle incorrect, give it a warning
    - If the user keeps making mistake, we want to keep asking for the correct input, until correct.
2. Make a loop that loops through # height times (Layers)
    - for layer in height times
3. During the loop, use another nested to construct the width amount stars per layer
    - end="" to print in the same line

"""

widthinput = int(input("How long do you want your rectangle's width to be?"))
heightinput = int(input("How long do you want your rectangle's height to be?"))
characterinput = input("Which character do you want to use to print out your rectangle?")

while len(characterinput) != 1:
    print('We cannot print that, please try again:')
    characterinput = input("Which character do you want to use to print out your rectangle?")


# for _ in range(heightinput):
#     # The heightinput is how many layers you want
#     print(widthinput * characterinput)

for height in range(heightinput):
    for width in range(widthinput):
        print(characterinput, end="");
    print('')
    
    
      




