a=input()
if len(a)<6:
    for i in a:
        print (i, end=" ")
else:
    for i in range (len(a)//2):
        print (a[i], end=" ")
