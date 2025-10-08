a=float(input("Give me a number"))
a=a**2
l=[x for x in range(int(a))]
print("Original List :", l)
count=0
for i in l:
    count+=i
avg=count/len(l)
print("sum=", count)
print("average =", avg)
l.sort()
print("Smalleest element is:", l[0])
print("Largest element is:", l[-1])