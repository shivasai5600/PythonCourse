""" In python there are 3 special functions
==> filter(), map() and reduce()    """
"""filter() ==> Is used for 'filtering out some elements from list of elements by applu=ying to function'"""
#========syntax : varname = filter(funname, iterated_object)
# here 'varname' is an object of type <class,filter> and we can convert into any iterable object by using type casting functions
# functional name represents either Normal function or anonymous function.
# 'iterable_object' represents sequence,list,set and dict types
"""The execution process of filter() is "Each value of iterable_object sends to function name. If the function return TRUE then the
element will be filtered,If the function return FALSE then the element will be neglected". This process will be 
continued until all elements of iterable objects completed."""
# ========== EXAMPLE ------------ 1 ====================
lst=[10,20,-30,-34,44,77,-45]
def decide(n):
    if n>0:
        return True
    else:
        return False
# main program
a=filter(decide,lst)
print("Type of a=",type(a))
print("Content of a=",a)
# convert object into list
plist = list(a)
print("Positive Elements =",plist)

print("="*60)

# ============= ANOTHER WAY OF WRITING OF ABOVE EXAMPLE ================
decide=lambda n:n>0
lst=[10,20,-30,-34,44,77,-45]
# main program
a=filter(decide,lst)
print("Type of a=",type(a))
print("Content of a=",a)
# convert object into list
plist = list(a)
print("Positive Elements =",plist)

print("="*60)

# ============= ANOTHER WAY OF WRITING OF ABOVE EXAMPLE ================
lst=[10,20,-30,-34,44,77,-45]
a=filter(lambda n:n>0,lst)
ps=tuple(a)
print("Tuple of list of elements",ps)

print("="*50)

# ==================== EXAMPLE ------  2====================
# n=int(input("Enter how many elements you want:" ))
# if n<=0:
#     print(f"{n} is invalid")
# else:
#     lst=[]
#     print("="*50)
#     print(f"Enter {n} elements")
#     print("=" * 50)
#     for i in range(1,n+1):
#         val=int(input())
#         lst.append(val)
#     else:
#         print("=" * 50)
#         print("Original Elements of list:{}".format(lst))
#         print("=" * 50)
#         pslist = list(filter(lambda n: n > 0, lst))
#         nslist= set(filter(lambda k: k < 0, lst))
#         zerolist = tuple(filter(lambda k: k==0, lst))
#         print(f"Positive Elements: {pslist}")
#         print(f"Negative Elements: {nslist}")
#         print(f"Zero Elements: {zerolist}")

print("="*50)

# ==================== EXAMPLE ------  2, Anotherway of explanation====================
# print("Enter List of elements are seperated by space:")
# lst = [int(x) for x in input().split()]                  # List comprehensive
# print("=" * 50)
# print("Original Elements of list:{}".format(lst))
# print("=" * 50)
# pslist = list(filter(lambda n: n > 0, lst))
# nslist= set(filter(lambda k: k < 0, lst))
# zerolist = tuple(filter(lambda k: k==0, lst))
# print(f"Positive Elements: {pslist}")
# print(f"Negative Elements: {nslist}")
# print(f"Zero Elements: {zerolist}")

print("="*70)
""" map() ==> it is used for obtaining new iterable object from existing iterable object by applying old iterable element 
to the function.
==> In otherwords, map() is used for obtaining new list of elements from exisitng list of eelments by applying old list of elemets
 to the function.
 
 == Syntax: varname= map(functionname, iterable_object)
 ==> here 'varname' is an object of type <class,map> and we can convert into any iterable object by using type 
    casting functions.
==> Functionname represents either normal function or anonymous function.
==> 'Iterable object' represents sequence,list,set and dict types.
==> The excecution process of map() is that 'map() sends every element of iterable object to the specified function,
process it and returns the modified value (result) and new list of elements will be obtained'. THis process will be continued 
until all elements of iterable objects completed."""

#=========================== EXAMPLE -- 1 ======================
"""def hike(sal):                # Normal function
    sal=sal+sal*(2/100)      # sal=sal(1+0.02), sal*1.02
    return sal
# main program
oldsallist = [10,20,30,40]
obj=map(hike,oldsallist)
print("Type of obj=",type(obj))
newsallist= list(obj)
print("Old salary list={}",format(oldsallist))
print("New salary list={}",format(newsallist))

print("="*50)
#=========================== EXAMPLE -- 2 ======================
hike=lambda sal:sal*1.02              # Anonymous function
# main program
oldsallist = [10,20,30,40]
newsallist= list(map(hike,oldsallist))
print("Old salary list={}",format(oldsallist))
print("New salary list={}",format(newsallist))

print("="*50)
#=========================== EXAMPLE -- 3 ======================
# main program
oldsallist = [10,20,30,40]
newsallist= list(map(lambda sal:sal*1.02,oldsallist))
print("Old salary list={}",format(oldsallist))
print("New salary list={}",format(newsallist)) """

print("="*50)
#=========================== EXAMPLE -- 4 ======================
""" write a program for suqare of a  number, cube of number """
"""print("Enter the elements you want that are seperated:")
lst=[float(x) for x in input().split()]
sqlist=tuple(map(lambda x:x**2,lst))
cblist=tuple(map(lambda x:x**3,lst))
print("="*50)
print("GivenNumber\tSquare\tCube")
print("="*50)
for n,q,t in zip(lst,sqlist,cblist):
    print("\t{}\t{}\t{}".format(n,q,t)) """

print("="*50)
# =========================== EXAMPLE -- 5 ======================
""" write a program for suqare of a  number, cube of number """
"""print("Enter the elements you want that are seperated by space:")
lst = [int(val) for val in input().split()]
poslist = tuple(map(lambda x: x ** 2,list(filter(lambda val:val>0,lst))))
neglist = tuple(map(lambda x: x ** 3,list(filter(lambda val:val<0,lst))))
print("Original list=",lst)
print("Positive list=",poslist)
print("Negative list=",neglist)  """

print("=" * 50)

""" reduce() : It is used for obtaining a single element / result from givrn iterable object by applying  to a function
==> syntax: varname = reduce(funname,iterable_object), here varname is an obj of int,float,bool,complex,str types
==> INTERNAL FLOW OF REDUCE
STEP-1 => reduce() selects two first values int place them First var and the Second var
STEP-2 => Function name utilizes the values First var and Second var applied to the specified object and obtains the result
STEP-3 => reduce() places the result of function namein first varaible and reduce() selects the succeding element of iterable
object and places in the second variable
STEP-4 => repeat step 2 and step 3 untill all elements completed in the iterable object and returns the result."""
# ================ EXAMPLE -1 ===============* SUM OF CONSECUTIVE VALUES
import functools
print("Enter the elements you want that are seperated by space:")
lst = [int(val) for val in input().split()]
res =functools.reduce(lambda x,y:x+y,lst)
print("type of res=",type(res))
print("sum=",res)

print("="*50)
# ================ EXAMPLE --2 ===============* COMPARE MAX AND MIN OF VALUES
import functools
print("Enter the elements you want that are seperated by space:")
lst = [int(val) for val in input().split()]
res =functools.reduce(lambda x,y:x if x>y else y,lst)
minm =functools.reduce(lambda x,y:x if x<y else y,lst)
print("max=",res)
print("min=",minm)

print("="*50)
# ================ EXAMPLE --3 ===============* COncatinaton of two words
import functools
print("Enter the words you want that are seperated by space:")
lst = [str(val) for val in input().split()]
res =functools.reduce(lambda x,y:x+" "+y,lst)
print("List of words={}".format(lst))
print("sum=",res)