a=input()
if a[1]=="к" or a[1]=="и" or a[1]=="л":
    for i in range (1, len(a), 2):
        print (a[i], end=" ")
else:
    for i in range(0, len(a), 2):
        print(a[i], end=" ")
