a=input()
for i in range(1, len(a), 2):
    if a[i]!="п" and a[i]!="и" and a[i]!="о":
        print(a[i], end=" ")
print()
for i in range(0, len(a), 2):
    if a[i]!="п" and a[i]!="и" and a[i]!="о":
        print(a[i], end=" ")
