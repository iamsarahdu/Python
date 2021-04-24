n=int(input("Enter the number"))
for I in range(1, n+1):
    for J in range(1,I+1):
        print(J%2,end="")
    print()