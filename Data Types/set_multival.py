#methods of set

#9. add()
st={22,55,77,99.5,'bye'}
print(st)
st.add(33)
print(st)
st.add(('hello',89))
print(st)
print("-----------------------------")
#10. update()
st={22,55,77,99.5,'bye'}
print(st)
st.update({34,35,65,'hello'})
print(st)
st.update({99})
print(st)
print("-----------------------------")
#11. discard()
st={22,55,77,99.5,'bye'}
print(st)
st.discard(99.5)
print(st)
st.add(('hello',89))
print(st)
st.discard(('hello',89))
print(st)
print("-----------------------------")
#12. remove()
st={22,55,77,99.5,'bye'}
print(st)
st.remove(77)
print(st)
st.remove(99)    
print(st)      #key error
print("-----------------------------")

#13. pop()
st={22,55,77,99.5,'bye'}
print(st)
st.pop()
print(st)
st.add(89)
print(st)
st.pop()
print(st)
print("-----------------------------")
#14. clear()
st={22,55,77,99.5,'bye'}
print(st)
st.clear()
print(st)
print("-----------------------------")
#15. del
st={22,55,77,99.5,'bye'}
print(st)
del str
print(st)
print("-----------------------------")
#16. issuperset()
s1={22,55,77,99.5,'bye'}
s2={22,55}
s3={'hello',99.5}
print(s1.issuperset(s2))
print(s1.issuperset(s3))
print(s1.issuperset({22,55,77,99.5,'bye'}))
print("-----------------------------")
#17. issubset()
s1={22,55,77,99.5,'bye'}
s2={22,55}
s3={'hello',99.5}
print(s2.issubset(s1))
print(s2.issubset(s1))
print(s3.issubset({22,55,77,99.5,'bye'}))
print("-----------------------------")
#18. isdisjoint()
s1={22,55,77,99.5,'bye'}
s2={22,55}
s3={'hello'}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
print(s3.isdisjoint({22,55,77,99.5,'bye'}))
