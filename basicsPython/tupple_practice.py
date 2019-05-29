tpl = (40, 50, 40, "xyz")
print(tpl)

single_tpl = (40,)
print(type(single_tpl))

single_tpl1 = (40)
print(type(single_tpl1))

print(tpl[3])
print(tpl*3)
print(tpl.count(40))
print(tpl.index("xyz"))

lst = [67, 34, "xyz"]
print(type(lst))
tpl_list = tuple(lst)
print(type(tpl_list))
print(tpl_list)
