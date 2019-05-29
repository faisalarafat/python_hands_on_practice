s = {10,20,30,"xyz",10,40,30}
print(s)
print(type(s))
s.update([88,99])
print(s)
print(type(s))

#print(s[0]) #'set' object is not subscriptable

#print(s[0:5]) #'set' object is not subscriptable

#print(s*3) #unsupported operand type(s) for *: 'set' and 'int'

s.remove(30)
print(s)

f =frozenset(s)
#f.update(s[0])
#f.remove(3)


