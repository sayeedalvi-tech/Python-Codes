#Methods
#Accessing the values from dict
#1. key value syntax
dic={'name':'Sayee',34:89,'age':20}
print(dic['name'])

#2. get()
print(dic.get(34))
print(dic.get('sal','Key is not present'))

#accessing only keys,only items,and only values\
#3. Accesssing only keys
dic={'name':'Sayee',34:89,'age':20}
print(dic.keys())

#4. Accessinhg only values
print(dic.values())

#5. Accessing only items
print(dic.items())

print(dir(dict))
#Adding the elements
#6.. Key-value pair syntax
d={'a':10,'b':20,'c':30}
print(d)
d['e']=50         # add new elememt
print(d)
d['c']=33         #modify exsisting element
print(d)

#7.update()
d={'a':10,'b':20,'c':30}
print(d)
d.update({'e':50})		# add single element
print(d)
d.update({'f':60,'g':70,'h':80})		#add multiple element
print(d)
d.update({'b':22,'a':11})		#modify/update exsisting element
print(d)

#8. setdefault()
d={'a':10,'b':20,'c':30}
print(d)
d.setdefault('e',50)      #add new element
print(d)
d.setdefault('h')		#add without value
print(d)
d.setdefault('b',22)     #cannot modify the exsisting values
print(d)

#9. fromkeys()
print(dict.fromkeys([55,26,32,88]))
print(dict.fromkeys([68,22,36],'hi'))
print(dict.fromkeys('hello',88))

#10. pop()
d={'a':10,'b':20,'c':30}
print(d)
d.pop('a')
print(d.pop('e','Key not present'))
print(d)

#11. popitem()
d={'a':10,'b':20,'c':30}
print(d)
d.popitem()
print(d)

#12. clear
d={'a':10,'b':20,'c':30}
print(d)
d.clear()
print(d)

#13. del
d={'a':10,'b':20,'c':30}
print(d)
del d
print(d)

#14. copy
#normal copy
#shallow copy
#Deep copy