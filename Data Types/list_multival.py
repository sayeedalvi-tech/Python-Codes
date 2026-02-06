'''
#list
#indexing
lst=[40,2.02,'Indumati',True,0.002,['raju','bheem'],['jaggu','chutki'],80]
print(lst[5][0])
print(lst[6][0][2:4:1])

lt=[[[[['Katrina']]]]]
print(lt[0][0][0][0][0])

ls=[['bye',90],[55,8.9,[98,'sizuka',[98,78]]]]
print(ls[1][1])
print(ls[1][2][2][1])
print(ls[1][2][1][4:-5:-1])
print(ls[1][2][1][-2:1:-1])

ll=[[[[[[['nobita']]],'sizuka']],89,'Chutki']]
print(ll[0][0][0][0][0][0][0])
print(ll[0][1])
print(ll[0][0][0][1])
print(ll[0][0][0][1][1::2])
print(ll[0][0][0][1][-5::2])


print(dir(list))


'''
'''
#list methods

#1. append()
lis=[23,78,9.5,True,'hello']
lis.append(50)
lis.append([52,'world'])
lis.append((92,85,'hell'))
print(lis)


#2. extend()
lis=[23,78,9.5,True,'hello']
lis.extend([52,'world'])
print(lis)
lis.extend('bye')
print(lis)
lis.extend([[92]])
print(lis)
lis.extend(([92],))
print(lis)


#3. insert()
lis=[23,78,9.5,True,'hello']
lis.insert(2,99)
print(lis)

lis=[23,78,9.5,True,'hello']
lis.insert(2,99)
print(lis)

#4. pop()

lis=[23,78,9.5,True,'hello']
lis.pop()
print(lis)

lis.pop(2)
print(lis)

ll=[1,66,'hi',[34,89,'bye',8.7]]
ll[3].pop(2)
print(ll)

#5. remove()
lis=[23,78,9.5,True,'hello']
lis.remove(True)
print(lis)

#6. clear()
lis=[23,78,9.5,True,'hello']
lis.clear()
print(lis)

#7. del
lis=[23,78,9.5,True,'hello']
del lis
print(lis)

#8. count()
ll=[89,809,89,5.6,True,89]
print(ll.count(89))

#9. index()
ll=[89,809,89,5.6,True,89]
print(ll.index(89))
print(ll.index(89,1))
print(ll.index(89,4,6))

#10. reverse()
#11. sort

# --** ASCII Conversions **--
# char to ASCII
print(ord('c'))
print(ord('S'))
print(ord('&'))
print(ord('0'))

#ASCII to char

print(chr(98))
print(chr(83))
print(chr(38))
print(chr(48))

lis=[25.5,89,63,53.2,[[True,'Yes'],[False,'No']],69]
lis[4][0].append(0)
print(lis)
lis[4][1].insert(3,1)
print(lis)
lis.extend([[89,58,63]])
print(lis)
print(lis.count(89))
lis.pop()
print(lis)
lis.remove(89)
print(lis)
lis.pop(3)
print(lis)
lis.sort()
print(lis)
lis.sort(reverse=True)
print(lis)

ll=['Sayee','Annanya','Mangesh','Ekansh','raj','tanvi']
ll.sort()
print(ll)
ll.sort(key=len,reverse=False)
print(ll)
ll.sort(key=len,reverse=True)
print(ll)

lis=[25.5,89,63,53.2,[[True,'Yes'],[False,'No']],69]
lis.extend(([89,36],))
print(lis)

#12. copy
#normal copy
l=[10,20,30,[40,50]]
ll=l
print(id(l))
print(id(ll))
l[1]=2
print(l)
print(ll)

ll[3][0]=4
print(l)
print(ll)

#shallow copy
l=[10,20,30,[40,50]]
ll=l.copy()
print(l)
print(ll)
print(id(l))
print(id(ll))

print(id(l[3]))
print(id(ll[3]))

l[0]=4
print(l)
print(ll)

l[3][1]=5
print(l)
print(ll)

#deep copy
from copy import deepcopy
l=[10,20,30,[40,50]]
ll=deepcopy(l)
print(l)
print(ll)
print(id(l))
print(id(ll))

print(id(l[3]))
print(id(ll[3]))

l[0]=4
print(l)
print(ll)

ll[3][1]=5
print(l)
print(ll)
'''
# 3 ways to merge 2 lists