# string(indexing)
'''s='hello'
for i in range(0,len(s)):
	print(s[i])'''

#write a prog to print the foll(using positive index)
'''s='How Are You?'
for i in range(0,len(s)):
	print(s[i])'''

#write a prog to print the foll(using negative index)
'''s='Good Afternoon'
print(s[-1]) #n
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])
print(s[-7])
print(s[-8])
print(s[-9])
print(s[-10])
print(s[-11])
print(s[-12])
print(s[-13])
print(s[-14])'''

'''s='Good Afternoon'
for i in range(-len(s),-1,-1):
	print(s[i],end='')'''


#str slicing positive index
'''
s="Hello Everyone!"
print(s[::])
print(s[2::])
print(s[:5:])
print(s[6:9:])
print(s[11:14:])
print(s[6:11:])
print(s[6:15])
print(s[::2])
print(s[2:12:3])
print(s[14:])
print(s[6:])
'''
#str slicing negative  index
'''s="Hello Everyone How Are You!!"
print(s[::-1]) #!!uoY erA woH enoyrevE olleH
print(s[-1::-1]) #!!uoY erA woH enoyrevE olleH
print(s[-1:-20:-1])# !!uoY erA woH enoyr
print(s[:-27:-1]) # !!uoY erA woH enoyrevE oll
print(s[-24::-1]) #olleH
print(s[-15:-23:-1]) #enoyrevE
print(s[-11:-14:-1]) #woH
print(s[-7:-10:-1])#erA
print(s[-3:-6:-1]) #uoY
print(s[::-2]) #!uYeAwHeorv le
print(s[-1::-4]) #!YAHovl
print(s[-1:-10:-2]) #!uYeA

#str slicing by combination of both forard and backward
s="Hello how are"
#forward(+ve,-ve) ei+1
print(s[1:-10+1:1])  #ell
print(s[6:-3+1:4])   #ha
print(s[1:-2+1:5])   #ehr
print(s[10::1])   #are

#forward(-ve,+ve)   ei+1
print(s[-12:11+1:5])  #ehr
print(s[-3:12+1:1])   #are

#backward(+ve,-ve)   ei-1
print(s[4:-12-1:-1])  #olle
print(s[8:-9-1:-2])   #who
print(s[2:-13-1:-1])  #leH

#backward(-ve,+ve)   ei-1
print(s[-9:1-1:-1])   #olle
print(s[-5:4-1:-2])   #who
print(s[-11::-1])     #leH

'''

'''
s="HEllo"
s[2]='L'
print(s[2]) #error....string is immutable...elements cannot be changed.
'''

#string Methods.
'''
#1. upper()
name='sayee'
print(name)
newname=name.upper()
print(newname)

#2. lower()
name='SAYEE'
print(name)
newname=name.lower()
print(newname)

#3. swapcase()
name='Sayee Dalvi'
print(name)
newname=name.swapcase()
print(newname)

#4. count()
name='Saayeeeeeeee'
print(name)
print(name.count('e',0,6))
print(name.count('a'))

msg="Hello hi How are You hi"
print(msg)
print(msg.count("hi"))
print(msg.count("h"))
print(msg.count("h",6))
print(msg.count("h",6,19))

s="Hello"
print(s.count("A"))
'''
'''
#5. index
ss="Hello How are You"
print(ss.index("How"))
print(ss.index("H"))
print(ss.index("H",0,9))
print(ss.index("ARE"))

# 6. find()
ss="Hello How are You"
print(ss.find("ARE"))

# 7. rindex()
s="Apple,Banana,Orange,Banana"
print(s.rindex("Banana"))
print(s.rindex("Pineapple"))

#8. rfind()
s="Apple,Banana,Orange,Banana"
print(s.rfind("Banana"))
print(s.rfind("Pineapple"))

#9. capitalize()
s="the haunted house"
print(s.capitalize())

#10. title()
s="the haunted house"
print(s.title())

#11. isalpha()
s="sayee"
print(s.isalpha())
s1="sayee1234"
print(s1.isalpha())
s2="sayee@#$%"
print(s2.isalpha())
print("sayee@1234".isalpha())

#12. isdigit()
s="1234"
print(s.isdigit())
s1="1234sayee"
print(s1.isdigit())
s2="1234@#$%"
print(s1.isdigit())
print("sayee@1234".isdigit())


#13. isalnum()
s="sayee13234"
print(s.isalnum())
s1="sayee"
print(s1.isalnum())
s2="13234"
print(s2.isalnum())
s3="@345"
print(s3.isalnum())
s4="@say"
print(s4.isalnum())
print("@#$%".isalnum())


#14. isupper()
s="SAYEE"
print(s.isupper())
s1="Sayee"
print(s1.isupper())
s2="SAY123"
print(s2.isupper())
s3="Say123"
print(s3.isupper())
print("SAY@123".isupper())


#15. islower()
s="sayee"
print(s.islower())
s1="SaYeE"
print(s1.islower())
s2="say123"
print(s2.islower())
s3="Say123"
print(s3.islower())
print("say@123".islower())


#16. isspace()
s="   "
print(s.isspace())
s1=""
print(s1.isspace())
s2="Sayee Dalvi"
print(s2.isspace())
print("1234".isspace())


#17. replace()
s="hi hello how are how you how"
newstr=s.replace("how","HOW",2)
print(newstr)
s1="helllooo"
newstr1=s1.replace("l","!",2)
print(newstr1)


#18. startswith()
s="hi hello hi are how you how"
print(s.startswith("hi"))
s1="hi hello hi are how you how"
print(s1.startswith("hi",9))
s2="hi hello hi are how you how"
print(s2.startswith("hello"))
s3="hello hi are how you how"
print(s3.startswith("he",0,2))


#19. endswith()
s="hi hello hi are how you how"
print(s.endswith("how"))
s1="hi hello hi"
print(s1.endswith("hi",9))
s2="hi hello hi are how you how"
print(s2.endswith("hello"))
s3="hello how is"
print(s3.endswith("is",6,12))


#20. strip()
s="    bye    "
print(s)
print(s.strip())

st="* 9jAK994"
print(st.strip(' HelloAbhi2@479 '))

st1="Python2586*9&j "
print(st1.strip('OKPy869257j* '))

#21. rstrip()
st1="Python2586*9&j "
print(st1.rstrip('OKPy869257j* '))

#22. lstrip()
st1="Python2586*9&j "
print(st1.lstrip('OKPy869257j* '))


#23. istitle()

#24. isindentifier()

#25. join()
s="sayee"
print(" ".join(s))m,,m

s1="hello"
print("*$".join(s1))

print("@".join("how are you"))


#26. split()

s="hello world ! ! !"
print(s.split())

s1="hello world ! ! !"
print(s.split('l'))

s2="hello world ! ! !"
print(s.split('l',2))


#.27 rsplit()

#28. removeprefix()
s="hello how are you?"
print(s.removeprefix('hello'))

#29. removesuffix()`
s1="hello how are you?"
print(s1.removesuffix('you?'))
'''