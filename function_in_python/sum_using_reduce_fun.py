from functools import reduce
lst = [5,25,15,35,20]
result = reduce(lambda x,y:x+y, lst)
print(result)