a=input()
if a[0]=="а" or a[0]=="э" or a[0]=="е" or a[0]=="я":
    for i in a:
        print (i, end=" ")
else:
    a=a[::-1]
    for i in a:
        print (i, end=" ")
