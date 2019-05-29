lst = [25,65,84,79,35,15,66,88,44,22,24]
result = list(filter(lambda x:x%2==0,lst))
print(result)
for i in result:
    print(i)