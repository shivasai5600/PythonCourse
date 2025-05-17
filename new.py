# a = int(input("enter the value a:"))
# b = int(input("enter the value b:"))
#
# print("sum is: {}".format(a+b))
# print("diff is: {}".format(a-b))
#
# print("=========================================")
# n = int(input("enter the value:"))
# if n<=0:
#     print(f"{n} is invalid")
# else:
#     lst=list()
#     for x in range(1,n+1):
#         val = input("enter {} value: ".format(x))
#         lst.append(val)
#     else:
#         print(lst)
# print("=========================================")
# n = int(input("enter the value:"))
# if n<=0:
#     print(f"{n} is invalid")
# else:
#     lst=list()
#     for x in range(1,n+1):
#         val = float(input("enter {} value: ".format(x)))
#         lst.append(val)
#     else:
#         print(lst)
#         print("----------------------------------------")
#         s=0
#         for val in lst:
#             print("{}".format(val))
#             s=s+val
#         else:
#             print(f"sum is: {s}")
#             print(f"avg is: {s/n}")
#
print("=====================================")
#
# c = int(input("enter the number for factorial: "))
# s=1
# for i in range(1,c+1):
#     print("value is : {}".format(i))
#     s=s*i
# else:
#     print(f"factorial of {c} is {s}")       # factorial program

print("==============inner/nested for loop=======================")
# for i in range(1,4):
#     print("outer loop {}".format(i))
#     for j in range(1,4):
#         print("===inner loop {}".format(j))      # for in for loop
#     else:
#         print(" out of inner loop ")
# else:
#     print("out of outer loop ")
print("==============================")
# for i in range(1,4):
#     print("outer loop {}".format(i))
#     j=1 #intialization
#     while j<=3:
#         print("===inner loop {}".format(j))     # while in for loop
#         j+=1
#     else:
#         print(" out of inner loop ")
# else:
#     print("out of outer loop ")
# print("==============================")
# i = 1 #initialization method
# while i<=3:
#     print("outer loop {}".format(i))
#     i += 1
#     for j in range(1,4):
#         print("===inner loop {}".format(j))     # for in while loop
#     else:
#         print(" out of inner loop ")
# else:
#     print("out of outer loop ")

print("==================================")
b = int(input("Enter the number: "))

if(b<=1):
    print(f"{b} is invalid")
else:
    result = False
    for i in range(2,b):
        if (b%i==0):
            result = True
            break
    if(result):
        print(f"{b} is not prime")
    else:
        print("{} is prime".format(b))      # prime or not of a number0