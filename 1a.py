#1(a)

l = []
lnew= []
num = int(input("Enter no. of elements "))
for i in range(num):
    el = int(input("Enter element "))
    l.append(el)
print("List is ", l)

for i in range(len(l)):

    for j in range(i+1,len(l)):
        lnew.append([l[i],l[j]])

print(lnew)