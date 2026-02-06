#1. WAP to check if the data is single valued data
a=eval(input("Enter Data:"))
if type(a) in (int,float,complex,bool):
    print(f"{a} is single valued datatype with datatype as {type(a)}")
else:
    print(f"{a} is not single valued datatype as {a} is {type(a)}")

if isinstance(a,(int,float,complex,bool)):
    print(f"{a} is single valued datatype with datatype as {type(a)}")
else:
    print(f"{a} is not single valued datatype as {a} is {type(a)}")


#2. WAP to check if given word is palindrome print yes else reverse the word
a=eval(input("Enter String:"))
if a[::-1]==a:
    print("Yes")
else:
    print(a[::-1])

#3. WAp to check the given char is lowercase then convert to title else print as it is
a=eval(input("Enter String:"))
if a.islower():
    print(a.title())
else:
    print(a)

#4. Wap to check length of dict if length is even print done else add one key value pair
a=eval(input("Enter Dictionary:"))
if len(a)%2==0:
    print("DONE")
else:
    k=eval(input("Enter Key:"))
    v=eval(input("Enter Value:"))
    a[k]=v
    print(a)

#5.Wap to check the iven number is even or odd
a=int(input("Enter NUmber:"))
if a%2==0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")

if (a//2)*2==a:
    print(f"{a} is even")
else:
    print(f"{a} is odd")

#6. wap to check the male and female are eligible for wedding
m=int(input("Enter Male's Age:"))
n=int(input("Enter Female's Age:"))
if m >=21 and n>=18:
    print("Eligible")
else:
    print("Not Eligible")

#7. WAp to return uppercase if the char is lower else retrun same char
a=eval(input("Enter String:"))
if a.islower():
    print(a.upper())
else:
    print(a)

#8. WAp to return lowercase if the char is upper else retrun same char
a=eval(input("Enter String:"))
if a.isupper():
    print(a.lower())
else:
    print(a)

#9. wap to find greater value among 2 number
num1=int(input("Enter 1st Number:"))
num2=int(input("Enter 2nd Number:"))
if num1 > num2 :
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

#10. wap to check if number is even or not, if not even then add+1 and make it even
a=int(input("Enter NUmber:"))
if a%2!=0:
    print(f"To Make it Even add 1---> {a+1}")
else:
    print("Even Number")

#11. WAP to check whether the string strting with uppercase or not if not then capitalize it
a=eval(input("Enter String:"))
if a[0].isupper():
    print(f"{a[0]} is upper")
else:
    print(a.capitalize())

#12. WAP to check if even number , if even reduce to half else make exponent
a=int(input("Enter NUmber:"))
if a%2==0:
    print(f"Reduced to half-->{a/2}")
else:
    print(f"Created Exponent-->{a**a}")

#13. WAP to check number should be divisible by 3 and 7
a=int(input("Enter NUmber:"))
if a%3==0 and a%7==0:
    print(f"{a} is divisible by both 3 and 7")
else:
    print("Not Divisble")

#14. Wap if the len is even then reverse else convert to upper case
a=eval(input("Enter String:"))
if len(a)%2==0:
    print(a[::-1])
else:
    print(a.upper())

#15. wap to number is pos or neg
a=int(input("Enter NUmber:"))
if a > 0:
    print(f"{a} is positive")
else:
    print(f"{a} is negative")

#16. WaP to check if data is single or collection dattype
a=eval(input("Enter String:"))
if type(a) in (int,float,complex,bool):
    print("Single Datatype")
else:
    print("Collection Datatype")

#17. WAP to check if specified charater is present in string
st=eval(input("Enter String:"))
c=eval(input("Enter Character:"))
if c in st:
    print("Present")
else:
    print("not Present")

#18. wap to check the length of dictionary and length of dictionary is even or Not if even
#print as it is or else add a item and make it even
#D={"a":"apple","b":"ball","c":"cat"}
a=eval(input("Enter Dictionary:"))
if len(a)%2==0:
    print(a)
else:
    k=eval(input("Enter Key:"))
    v=eval(input("Enter Value:"))
    a.update({k,v})
    print(a)

#19. wap to check the given number is greater than 5,if it is greater convert that number into negative number else print the same number
a=int(input("Enter Number:"))
if a >5:
    print(-abs(a))
else:
    print(a)

#20. wap to check the given number is smaller than 10 ,if it is smaller find the exponent of it else print the number as it is
a=int(input("Enter Number:"))
if a <10:
    print(a**2)
else:
    print(a)

#21. wap to check the given number is odd, if it is odd divide it by 2 and print reminder and quotient else print it is even (take user input)
a=int(input("Enter Number:"))
if a%2!=0:
    print(f"Quotient->{a/2}")
    print(f"Remainder->{a%2}")
else:
    print("It is even")

#22. wap to check if the given character is alphabets or Not ,if it is alphabet create a replica of it for 2 times. (take user input)
st=eval(input("Enter data:"))
if st.isalpha():
    print(st*2)
else:
    print("not alphabet")

#23. WAP to check whether the given number value is divisible by 6 or not,if it is divisible cube that number or else perform left shift operation by 3 (take user input)
a=int(input("Enter Number:"))
if a%6==0:
    print(a**3)
else:
    print(a<<3)