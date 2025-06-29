#1(c)

t = ()
num = int(input("Enter number of tuples "))
for i in range(num):
    ttemp = ()
    el = int(input("Enter no. of elements "))
    for j in range(el):
        elf = int(input("Enter element "))
        ttemp += (elf,)
    t += (ttemp,)
print(t)

t1 = (1,2,3,4)
t2 = (3,5,2,1)
t3 = (2,2,3,1)
tsum = ()
for i in range(len(t1)):
    a = t1[i] + t2[i] + t3[i]
    tsum += (a,)
print(tsum)

