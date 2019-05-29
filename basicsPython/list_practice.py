lst = [10,20.5, "Faisal", -10, 30]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst*2)
print(len(lst))

lst.append(40)
print(lst)
lst.remove('Faisal')
print(lst)
del(lst[0])
print(lst)

#lst.clear()
#print(lst)

print(max(lst))
print(min(lst))

lst.insert(3, 5)
print(lst)

lst.sort()
print(lst)

'''lst = ["Bangladesh", "USA", "India"]
lst.append("Japan")
lst.remove("USA")
lst.insert(1, "China")
print(lst)'''
