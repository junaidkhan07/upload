#nested for loop

string=input("enter the string\n")
lenght=len(string)
for row in range(lenght):
    for col in range(row+1):
        print(string[col],end="")
    print()