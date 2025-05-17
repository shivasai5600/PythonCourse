a = int(input("enter the number:"))
if a <= 10:
    print("true")
else:
    i = 1
    n = 20
    while(i <= n):
        print(i)
        i = i+1
print("================================================")

x = int(input("enter the number how many you want to represent until it:"))
if(x<=0):
    print("%d is less than zero" %d)
else:
    i = 1                 # initialization
    while(i<=x):          # condition
        print(i,end=" ")
        i = i+1           # updation
    else:
        print("\n=====================================================")

a = int(input("enter the table number you want:"))
for x in range(1,11):
    # print("{}X{}={}".format(a,x,a*x))                      # table using for loop
    print("%dX%d=%d" %(a,x,a*x))
print("===============================================")
f = int(input("Enter the number:"))
if(f<=0):
    print("it is lessthen zero")
else:
    i = 1                        # initialization
    while(i<=f):                 # condition
        print(f-i,end=" ")
        i = i+1                  # updation
        if f-i==0:
            break      # it is breaking the value zero at this point   o/p: 4 3 2 1
    print("\n=====================")
h = int(input("Enter the number:"))
if(h<=0):
    print("it is lessthen zero")
else:
    while(h>0):
        print(h,end=" ")
        h = h-1                        #o/p: 5 4 3 2 1
    else:
        print("\n===============================")

j = int(input("Enter the number:"))
if(j<=0):
    print("it is lessthen zero")
else:
    i = 2
    while(i<=j):
        print(i,end=" ")         # o/p: 2 4 6 8 10
        i = i+2
    else:
        print("\n===============================")

k = int(input("Enter the number:"))
if(k<=0):
    print("it is lessthen zero")
else:
    while(k>0):
        print(k,end=" ")      #o/p: 10 8 6 4 2
        k= k-2
    else:
        print("\n===============================")

m = int(input("Enter the number:"))
i = 1
while(i<=10):
    print(f"{m}X{i}={m*i}")       # table using while loop
    i = i+1
print("==========================================")
s = int(input("Enter the number:"))
if s<=0:
    print("invalid no. %d" %(s))
else:
    i,e = 1,0                # multiline statements
    while(i<=s):
        print(i)
        e=e+i
        i=i+1
    else:
        print(e)       # sum of n natural numbers
print("==============================================")
a = int(input("enter the nymber:"))
i=1
s=0
while(i<=a):
    # print(i)
    s=s+(i*i)
    i=i+1
    print(s)
print("=======================================")
a = int(input("enter the nymber:"))
i=1
s=0
while(i<=a):
    # print(i)
    s=s+i**2
    i=i+1
    print(s)


