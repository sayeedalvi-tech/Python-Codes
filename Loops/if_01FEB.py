#11. wap to check the given  character is uppercase then convert to lower case
a=input("Enter String:")
if a.isupper():
    print("Is Upper.")
    print(f"Converted to lower : {a.lower()}")

#12. wap to check the given char is in upper case and covert to lower case without string method
a="S"
if ord('A') <= ord(a) <= ord('Z'):
    print(chr(ord(a)+32))

#13. wap to check the given char is in loercase and covert to upper case
a=input("Enter String:")
if a.islower():
    print("Is Lower.")
    print(f"Converted to upper : {a.upper()}")

#14. wap to check the given char is in lowercase and covert to upper case without string method
a="c"
if ord('a') <= ord(a) <= ord('z'):
    print(chr(ord(a)-32))  

#15. wap to check the given character is string datatype
y=1
if type(y) == str:
    print("It Is a String") 
        
if isinstance(y,str):
    print("It Is a String")

#16. WAP TO CHECK IF IT A SINGLE VALUED TYPE
a=eval(input("Enter data: "))
if type(a) in (int,bool,float,complex):
    print(f"{a}----->Single Valued Data Type")

if isinstance(a,(int,bool,float,complex)):
    print(f"{a}----->Single Valued Data Type")

#17. WAP TO CHECK IF IT A MULTI VALUED TYPE
a=eval(input("Enter data: "))
if type(a) in (str,list,set,dict,tuple):
    print(f"{a}----->Multi Valued Data Type")

if isinstance(a,(str,list,set,dict,tuple)):
    print(f"{a}----->Multi Valued Data Type")

#18. PALINDROME OR NOT
a=eval(input("Enter data: "))
if a == a[::-1]:
    print(f"{a} is palindrome")

#19. WAP TO CHECK IF GIVEN CHARCTER IS EVEN SOTRED INSIDE A LIST
a=eval(input("Enter data: "))
lis=[]
if a%2==0:
    lis.append(a)
    print(f"{a} is even hence addes to list")
    print(lis)

if a%2==0:
    lis=lis+[a] or lis=+[a]
    print(lis)