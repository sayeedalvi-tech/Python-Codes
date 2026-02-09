# # #1. WAP TO CHECK IF NUMBER IS POSTIVE IF POSITIVE THEN CHECK IF EVEN OR ODD
# # num=int(input("Enter NUmber"))
# # if num > 0:
# #     if num%2==0:
# #         print("Positive and even")
# #     else:
# #         print("Positive and odd")
# # else:
# #     print("Negative number")

# #2. take list datatype, perform list operation 1-pop 2-sort 3-clear 4-invalid if other datatype invalid datatype
# data=eval(input("Enter Data:"))
# if type(data)==list:
#     ch=int(input("Enter Operation:\n1.pop\n2.sort\n3.clear\n"))
#     if ch==1:
#         a=data.pop()
#         print(f"Popped Element:{a}")
#         print(data)

#     elif ch==2:
#         data.sort()
#         print(f"Sorted List :{data}")

#     elif ch==3:
#         c=data.clear()
#         print(data)

#     else:
#         print("Invalid Operation")

# else:
#     print("Invalid datatype")

#3. WAP to book a ticket in book my show
print("WELCOME TO BOOK MY SHOW💕")
theatre=['PVR','INOX','CITY PRIDE','TALKIES','CINEPOLIS']
user=input("Enter Theatre Name:")
if user in theatre:
    print(f"Selected Theatre : {user}")
    movies=['YJHD','KKKG','KGF','PUSHPA','KKHH','ZNMD']
    user1=input("Enter Movie:")
    if user1 in movies:
        print(f"Selected Theatre : {user}")
        print(f"Selected Movie: {user1}")
        price=[200,300,400,500]
    else:
        print("Movie not available")
else:
    print("Theatre not present")
    