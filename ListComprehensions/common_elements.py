a = [2,4,6,8,10]
b = [1,2,3,4,5]
result=[]
'''for i in a:
    if i in b:
        result.append(i)
print(result)'''
result = [i for i in a if i in b]
print(result)