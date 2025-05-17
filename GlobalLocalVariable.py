
""" ==> The purpose of global variables is that, "to store common values for different function calls" 
==> Global variable are those, which are defined before all the functions.
==> Local Variables are those, which are used for storing Temporary results  in the function body.
==> Local variables are those , which are defined within the function body."""

""" Global and Local Variables ============ METHOD ------ 1     """
# lang = "Python"             #globalvarible
# def lernDatsc():
#     crs1 = "DataScience"     #localvarible
#     print("To develop '{}' based applications , we use '{}' language".format(crs1,lang))
# def lernML():
#     crs2 = "Machine Learning"     #localvarible
#     print("To develop '{}' based applications , we use '{}' language".format(crs2,lang))
# def lernDL():
#     crs3 = "Deep Learning"     #localvarible
#     print("To develop '{}' based applications , we use '{}' language".format(crs3,lang))
#
# lernDatsc()
# lernML()
# lernDL()
 # ==================================        METHOD ----2
# def lernDatsc():
#     crs1 = "DataScience"     #localvarible
#     print("To develop '{}' based applications , we use '{}' language".format(crs1,lang))
# def lernML():
#     crs2 = "Machine Learning"     #localvarible
#     print("To develop '{}' based applications , we use '{}' language".format(crs2,lang))
# def lernDL():
#     crs3 = "Deep Learning"     #localvarible
#     print("To develop '{}' based applications , we use '{}' language".format(crs3,lang))
#
# # main program
# lang="PYTHON" # global variable
# lernDatsc()
# lernML()
# lernDL()

                    # ========Example----1 global varaible and global keyword============
# when you want to modify the global variable, we need to refer with the global varaiable in the function of a
# function defenition of a function body.
# a=10 # global variable
# def increament():
#     global a     # refering global variable a, with 'global' as a keyword
#     print("line -> 43 val of a in increament = {}".format(a))  # accessing global variable
#     a=a+1
#     print("line -> 45 val of a in increament = {}".format(a))
#
# # main program
# print("line -> 48 val of a before increament-main program = {}".format(a))
# increament()
# print("line -> 50 val of a after increament-main program increament = {}".format(a))

# ========Example----2 global varaible and global keyword============

# a,b = 10,20 # here a,b are called global variables
# def updateval():
#     global a,b          # here 'global' is a keyword of global variable
#     a=a+1
#     b=b+1
# def updateval2():
#     global a,b
#     a=a*2
#     b=b*2
#
# #main program
# print(" val of a before increament-main program = {}".format(a))
# print(" val of b before increament-main program = {}".format(b))
# updateval()
# print(" val of a after increament-main program = {}".format(a))
# print(" val of b after increament-main program = {}".format(b))
# updateval2()
# print(" val of a after increament-main program = {}".format(a))
# print(" val of b after increament-main program = {}".format(b))

""" ============ GLOBAL VARIABLE AND LOCAL VARIABLE, AND GLOBAL FUNCTION ============="""
# a=10
# b=20
# c=30
# d=40
# def fun1(): # here a,b,c,d are global variables
#     global c,d
#     c=c+1
#     d=d+1
#     a=100
#     b=200      # here a, b are local variables
#     print(f"{a}")
#     print(f"{b}")
#     print(f"{c}")
#     print(f"{d}")
#     z= a+b+c+d
#
#     print(f"Result of a,b,c,d is {z}")
#
# # main  program
# fun1()

               # Example ---------2
# a=10
# b="python"
# c=23.44
# def fun2():
#     obj=globals()
#     print("type of obj=",type(obj))
#     for k,v in obj.items():
#         print(f"{k}==>{v}")
#     print("----------------------------------")
#     print(f"Print val of global variable a={obj.get("a")}")
#     print(f"Print val of global variable b=",obj.get("b"))
#     print("---------------OR-------------------")
#     print(f"Print val of global variable a={obj['a']}")
#     print(f"Print val of global variable b=",obj['b'])
#     print("---------------OR-------------------")
#     print(f"Print val of global variable a=",globals().get('a'))
#     print(f"Print val of global variable b=",globals().get('b'))
#     print("---------------OR-------------------")
#     print(f"Print val of global variable a=", globals()['a'])
#     print(f"Print val of global variable b=", globals()['b'])
# fun2()

#  ====== Example -1 continuation of getting global variable =========
# a=10
# b=20
# c=30
# d=40
# def fun1(): # here a,b,c,d are global variables
#     global c,d
#     c=c+1
#     d=d+1
#     a=100
#     b=200      # here a, b are local variables
#     print(f"local variable {a}")
#     print(f"local variable {b}")
#     print(f"global variable {c}")
#     print(f"global variable {d}")
#     print("global variable of a=",globals().get('a'))
#     print("global variable of b=",globals().get('b'))
#     z= a+b+c+d+globals().get('a')+globals().get('b')
#
#     print(f"Result of a,b,c,d is {z}")
#
# # main  program
# fun1()

#  ================   Example -----  3  ==========================
a,b,c,d = 1,2,3,4
def fun3():
    a,b,c,d = 10,20,30,40
    d1=globals()
    print(f"local variable {a}")
    print(f"local variable {b}")
    print(f"local variable {c}")
    print(f"local variable {d}")
    print("global variable of a=",d1.get('a'))
    print("global variable of b=",d1.get('b'))
    print("global variable of c=",d1.get('c'))
    print("global variable of d=",d1.get('d'))
    j=a+b+c+d+d1['a']+d1['b']+d1['c']+d1['d']
    print(j)

fun3()
