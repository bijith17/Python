#insertion,deletion not possible,ordered and indexed.

t1=(13,30.5,"abcd",20,"python",12)

print(t1)
print()
print(t1[0])
print()
print (t1[1:3])

t2=t1.count(12)
print(t2)

t3=t1.index(12)
print(t3)

l=list(t1)
l.append("sunday")
print(l)

t1=tuple(l)
print(t1)
del t1



