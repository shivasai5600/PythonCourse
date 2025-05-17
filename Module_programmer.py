""" ===========================  NUMBER OF APPROACHES OF MODULES ===========================

==> To Access the Function Names, variables and Class Names of Modules, we have two approaches.They are..
    a) By using 'import' statement
    b) By using 'from...import' statement
--------------------------------------------------------------------------------------------------------
a) By using 'import' statement
==> Here, 'import' is a keyword.
==> The purpose of import statement is that,'TO access the variables, functions, and class names in the current python program'
    with respect to Module Name/Alias Name.
==> This approach having 4 synatxs.They are
--------------------------------------------------------------------------------------------------------
========= Syntax--1 : importing single module name ==============
                       import module name
Examples : import calculation
           import circle
----------------------------------------------------------------------------------------------------------
========= Syntax--2 : importing modulename1, modulename2.......etc
                      import modulename1,modulename2,.....
Examples : import calculation,circle,
---------------------------------------------------------------------------------------------------------
========= Syntax--3 : importing single modulename as alias name ==============
                       import modulename as mn
Examples : import calculation as cal
           import circle as cr
------------------------------------------------------------------------------------------------------------
========= Syntax--4 : importing Multiple modulenames as alias names ==============
                       import modulename1 as mn, modulename2 as ma,.... modulenamen as mnn
Examples : import calculation as cal, circle as cc
-----------------------------------------------------------------------------------------------------------
==> After importing the module name with import statement then we must access the variables names, function names,
    and class names of the module w.r.t Module name otherwise we get name error.

    Module name.Variable name
    Module name.Function name
    Module name.Class name
-----------------------------------OR----------------------------------------
    Alias name of Module name.Variable name
    Alias name of Module name.Function name
    Alias name of Module name.Class name
===========================================================================================================================

b) By using 'from...import' statement
==> Here 'from' and 'import' both are keywords
==> The purpose of from..import statement is that,'TO access the variables, functions, and class names in the current python
    program' without using Module Name/Alias Name.
==> This approach having 3 synatxs.They are
--------------------------------------------------------------------------------------------------------
========= Syntax--1 : importing variable names, function names, and class names of single module ==============
                       from module name import var1,...varn, Funname1,...Funnamen, Classname1,...Classnamen
Examples : from calculation import addop,subop
--------------------------------------------------------------------------------------------------------
========= Syntax--2 : importing variable names, function names, and class names of module name as alias name ==============
                       from module name1 import varables as alias name, functions as alias name, class name as alias name
Examples : from calculation import addop as ad,subop as sb
           from math import sqrt as s, pi as k
--------------------------------------------------------------------------------------------------------
========= Syntax--3 : importing ALL variable names, function names, and class names of module name ==============
                       from module name import *
        here '*' represents a wild character and instructs the PVM to import all variable names,function names,classnames
        (THis syntax is not recommended bcz ir provides required variables, functions, and classes and also provides
        un-intrested variables, function names ans class names and leads more memory space and takes more execution time)
Examples : from calculation import *
---------------------------------------------------------------------------------------------------------------------------
==> After importing the module name with from..import statement then we must access the variables names, function names,
    and class names of the module without preceded with Module name or alias name.
                  Variable Name
                  Function Name
                  Class Name
"""

# import Modules              # ======= 1-- way of method
# Modules.addop(10,20)

# from Modules import addop         # ======= 2-- way of method, as it is accessing the entire program functions in file
# addop(10,20)

# from Modules import sortnames as s
# s()

from Modules1 import *
import sys
from Modules import menu
while True:
    menu()
    ch=int(input("Enter your choice:"))
    match(ch):
        case 1:
            addop()
        case 2:
            subop()
        case 3:
            mulop()
        case 4:
            divop()
        case 5:
            modop()
        case 6:
            expop()
        case 7:
            print("Thanks for using this program")
            sys.exit()
        case _:  # deafult case block
            print("Your choice of selection is wrong, please try again")
