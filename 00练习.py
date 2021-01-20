sing = ('a','b','c','d','e','f','g')
dance = ('g','f','s','d','a','r','c')
rap = ('g','e','y','i','t','h','r','a')
p_dict = {}
allPerson = sing + dance + rap
for name in allPerson:
    if name not in p_dict:
        p_dict[name] = allPerson.count(name)
print(p_dict)