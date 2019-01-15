arr="абвгдеёжзийклмнопрстуфхцчшщъыьэюяа"
a=input()
b=""
for i in range (len(a)):
    x=arr.find(a[i])
    b+=arr[x+1]
print(b)
