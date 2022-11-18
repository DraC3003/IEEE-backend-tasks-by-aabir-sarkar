count = 1
number = input("Enter the number of test cases: ")


while count <= int(number):
    mystring = input("Enter the string: ")

    n = input("Enter the length of the string: ")

    n1 = int(n)

    goodString = True

    for i in range(0, (n1//2)):
        if (list(mystring)[i] != list(mystring)[(n1//2)+i]):
            goodString = False
            break

    if goodString == True:
        print("Yes")
    else:
        print("No")

    count = count+1
