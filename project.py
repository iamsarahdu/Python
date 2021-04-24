userInput = input("Write something:")

ifUserWantsToQuit = userInput.capitalize() == "Quit"

# if userinput == 'quit':
#     print("Quiting because you told me to")
# else:
#     print(f"You said {userinput}")

while not ifUserWantsToQuit:
    print(f"You said {userInput}")
    userInput = input("Write something:")
    ifUserWantsToQuit = userInput.capitalize() == "Quit"

if ifUserWantsToQuit:
    print("You want to quit")
    
# while i != userinput:
#     input("Write something:")
#     print(f"You said {userinput}")
# if i == userinput:
#     print("Quiting because you told me to")


    