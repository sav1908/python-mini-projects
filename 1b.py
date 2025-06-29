#1(b)

d = {}
dnew = {}
num = int(input("Enter no. of elements in dict "))

for i in range(num):
    k = input("Enter key ")
    vnum = int(input("Enter no. of elements in list value "))

    l = []

    for j in range(vnum):
        el = int(input("Enter element for list "))
        l.append(el)
    d[k] = l

print('dict formed is ', d)

keyl = d.keys()
print(keyl)

for i in keyl:
    lnew = []
    for j in d[i]:
        if j%2 == 0:
            lnew.append(j)
    dnew[i] = lnew

print(dnew)