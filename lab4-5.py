a = {1,2,3,4,5,6,7,8,9}
b = {1,3,5}
c = {1,9,11,14,16}
print(a.union(b).union(c))
print(a | b | c)
print(a.intersection(b).intersection(c))
print(a & b & c)
print(a.difference(b).difference(c))
print(a - b - c)

