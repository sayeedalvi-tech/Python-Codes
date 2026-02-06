'''#indexing

#forwardslicing 
t=(25,98.2,'Hello',False,99)
print(t[1:4:2])
print(t[2][1:4:1])
print(t[::4])

#backward slicing
print(t[-1:-4:-2])

#combinatiomn
print(t[0::4])
print(t[-5:4+1:4])

#nested tuple
tup=('hii',(29,54.7,'Bheem','Nobita','Sizuka',False))
print(tup[0][1:3:1])
print(len(tup))
print(tup[1][2][2:4:1])
print(tup[1][3][-2:-5:-1])
print(tup[1][2][-1::-4])


tup1=('hii',(29,54.7,'Bheem','Nobita',('Sizuka','Gian'),False))
print(tup1[1][4][0][2::3])
print(tup1[1][4][1][::-1])


print(dir(tuple))

'''
# tuple methods

#1. count
t=(11,345,89.6,345,89,9,345,67)
print(t.count(345))

#2. index
t=(11,345,89.6,345,89,9,(345,67))
print(t.index(345))
print(t.index(89))
print(t[6].index(67))

#3.del

del t
print(t)