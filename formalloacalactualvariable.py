# def ss(a,d):                                           # formal parameter/variable
#     print("Enter the value of a:{}".format(a))
#     print("Enter the value of d:{}".format(d))
#     c=a+d                                              # Local variable/parameter
#     print(f"{a},{d} is {c}")
# # main program
# x=float(input("Enter the number:"))
# y=float(input("Enter the number:"))
# ss(x,y) # here x,y are actual parameters

""" positional parameter argument"""
# def dp(stno,name,marks):
#     print("{}\n{}\n{}".format(stno,name,marks)) # 1 way of writing
# stno=1
# sname="sai"
# marks=99
# dp(stno,sname,marks)
# print("="*70)
# dp(2,"shiva",100)

# print("="*70)
#                  # default parameter argument example====1
# def dp(stno,name,marks,city="HYD"):
#     print("{}\t{}\t{}\t\t{}".format(stno,name,marks,city)) # 1 way of writing
# print("="*60)
# print("No.\tName\tMarks\tCity")
# print("="*60)
# dp(1,"sai\t", 99)   # uses default city parameter
# dp(2,"shiva",100)
# dp(3,"ssss",98,"DVK")   # updating the city value
# print("="*60)

                 # default parameter argument example====2
# def arcircle(r,pi=3.14):
#     ac=pi*r**2
#     print("Radius is {}".format(r))
#     print("Area of Circle is {}".format(ac))
# print("="*60)
# arcircle(1.2)
# arcircle(2.2)
# arcircle(3.4)

                 # Keyword parameter argument example====3
# def ar(r,p,v,z="python"):
#     print("{}\t{}\t{}\t{}".format(r,p,v,z))
#
# # main program
# print("="*60)
# print("R\tP\tV")
# print("="*60)
# ar(10,20,30,"java")
# ar(p=20,v=30,r=10)          # function calling-----keyword arguments
# ar(10,v=30,p=20)         # function calling and keyword argument
# # ar(v=30,10,20)  , ar(p=20,v=30,r=10,"java")        # syntax error---here positional argument follows keyword arguments
# print("="*60)

               # variable length argument
# def dis(a):
#       print(a)
# def dis(a,c):
#     print(a,c)
# def dis(a,c,d):
#     print(a,c,d)
#
# dis(10)
# dis(10,20)
# dis(10,20,30)


               # variable length argument
# def dis(a):
#     print(a)
# dis(10)
# def dis(x,y):
#     print(x,y)                           # 2 - method
# dis(10,20)
# def dis(x,y,z):
#     print(x,y,z)
# dis(10,20,30)
               # pure variable length parameter/argument
# def dis(*a):
#     for val in a:
#         print("{}".format(val),end=" ")
#     print()
#     # print("Type of a is {} ".format(type(a)))        # 1-method
#     # print(a)
#
# dis(10)
# dis(10,20)
# dis(10,20,30)

                   # keyword variable length parameter    ======== Example ---1
# def dis( **a ):
#     print("="*50)
#     for k,v in a.items():
#         print("{} --> {}".format(k,v))
#
# #main program
# dis(sno=10,sname="mystudent",hobby="playing")

                   # keyword variable length parameter    ======== Example ---2
def totalmarks(sname,cls,**marks):
    print("Name of the student is {}".format(sname))
    print("Class of the student is {}".format(cls))
    print("="*50)
    print("SubjectName\tMarks")
    print("=" * 50)
    so=0
    for sn,ma in marks.items():
        print("\t{}\t\t{}".format(sn,ma))
        so=so+ma
    print("=" * 50)
    print("Total Marks = {}".format(so))
    print("=" * 50)

#main program
totalmarks("WE",10,te=99,hi=98,en=98,ms=100,sc=100)
totalmarks("I",11,sa=99,ma1=100,en=98,ma2=100,sc=100)