# Slices
# It is a way to make a copy of a list
# because if you do a = b, then a and b are the same list
# this is because a points to the same memory location
# but if you do c = a[:], then c is a copy of a

a = [1,2,3,4,5]
b = a

print(a)
print(b)

del a[0]
print(id(a))
print(id(b))

c = a[:]
print(id(a))
print(id(b))
print(id(c))

a.append(6)
print(a)
print(b)
print(c)
