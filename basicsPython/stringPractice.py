from list_practice import lst
s = "  This is a string for practice  "

print(s*2)

print(len(s))
print('i' in s)
print('s' in s)

print(s[0:])
print(s[3:8])
print(s[:7])
print(s[0:9:2])
#Reverse the string
print(s[::-1])

print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.find("str"),0,len(s)) #S.find(sub[, start[, end]])
print(s.find("w"),0,len(s))
print(s.count("a"))
print(s.replace("for", "to"))

print(s.upper())
print(s.lower())
print(s.title())

print(max(lst))
print(min(lst))

lst.insert(3, 35)
print(lst)

lst.sort()
print(lst)